def file_mover(executable):
    def _func():
        pass
    return _func

def os_linux_installer():
    file_mover_pkg = file_mover("mv")
    def _func():
        return
    def start():
        print("Started Linux Installer")
        return 
    _func.start = start
    return _func

def unsupported_os(os_name):
    name = os_name
    def _func():
        def start():
            raise RuntimeError(f"Failed: Trying to run this script in an unsupported operating system: \"{name}\"")
        _func.start = start
        return _func
    return _func

def get_os_installer(os_name):
    name = os_name.lower()
    installers = {
            "linux": os_linux_installer
    }
    return installers.get(name, unsupported_os(name))

def audit_install(os_name):
    if not isinstance(os_name, str):
        raise ValueError("OS Name must be a string")
    installer = get_os_installer(os_name)
    installer().start()

if __name__ == "__main__":
    try:
        import sys
        audit_install(sys.platform)
    except Exception as e:
        print(e)
        exit(1) # Exit with error
