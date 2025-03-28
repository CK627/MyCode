import sys
import subprocess

class ErrorHandler:
    @staticmethod
    def handle_import_error(e: ImportError, package: str = None):
        print(f"\n[错误] 缺少依赖 - {str(e).split()[-1]}")
        if package:
            print(f"尝试安装 {package}...")
            try:
                subprocess.check_call(
                    [sys.executable, "-m", "pip", "install", package],
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL
                )
                print(f"安装成功，请重新运行")
            except Exception:
                print(f"安装失败，请手动执行: pip install {package}")
        sys.exit(1)

    @staticmethod
    def handle_config_error(msg: str):
        print(f"\n[配置错误] {msg}")
        sys.exit(1)