import os
import sys
import subprocess
import time
import re
import signal

from colorama import Fore, Style, init
from pyfiglet import figlet_format

init(autoreset=True)

VERSION = "1.0"

RESET = Style.RESET_ALL
GREEN = Fore.GREEN
CYAN = Fore.CYAN
YELLOW = Fore.YELLOW
RED = Fore.RED
ELECTRIC_BLUE = "\033[38;5;39m"

TEMPLATES = {
    "01": ("Instagram", "/instagram/"),
    "02": ("Facebook", "/facebook/"),
    "03": ("LinkedIn", "/linkedin/"),
    "04": ("Gmail", "/gmail/")
}

flask_process = None
cloudflare_process = None
ngrok_process = None

cloudflare_url = None
ngrok_url = None


def clear():
    os.system("clear")


def pause():
    input(f"\n{CYAN}Press Enter to continue...{RESET}")


def banner():
    clear()

    title = figlet_format("SOCIOPHISHER", font="small")
    print(ELECTRIC_BLUE + title + RESET)

    print(
        f"{GREEN}[+] {CYAN}"
        "SOCIOPHISHER - Security Awareness Training Lab"
    )

    print(f"{GREEN}[+] {CYAN}Version : {VERSION}")
    print()


def about():
    banner()

    print(f"{CYAN}[::] About Sociophisher [::]{RESET}\n")

    print("Sociophisher is a local security-awareness")
    print("training simulator for learning about phishing")
    print("and identifying suspicious login pages.\n")

    print("Training environment:")
    print("  • Flask training server")
    print("  • Cloudflare Tunnel")
    print("  • ngrok Tunnel")
    print("  • No credential storage")
    print("  • Dummy training data only")
    print("  • Authorized security-awareness use only")

    pause()


def start_flask():
    global flask_process

    if flask_process is not None:
        return True

    print(f"{YELLOW}[*] Starting local training server...{RESET}")

    try:
        flask_process = subprocess.Popen(
            [sys.executable, "app.py"],
        )

        time.sleep(2)

        if flask_process.poll() is not None:
            print(f"{RED}[!] Flask server failed to start.{RESET}")
            flask_process = None
            return False

        print(f"{GREEN}[+] Flask server started.{RESET}")
        print(f"{GREEN}[+] Local server: http://127.0.0.1:5000{RESET}")

        return True

    except Exception as e:
        print(f"{RED}[!] Failed to start Flask: {e}{RESET}")
        return False


def start_cloudflare():
    global cloudflare_process
    global cloudflare_url

    if cloudflare_process is not None and cloudflare_url:
        return True

    print(f"{YELLOW}[*] Starting Cloudflare Tunnel...{RESET}")

    try:
        cloudflare_process = subprocess.Popen(
            [
                "cloudflared",
                "tunnel",
                "--url",
                "http://127.0.0.1:5000"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        url_pattern = re.compile(
            r"https://[a-zA-Z0-9-]+\.trycloudflare\.com"
        )

        start_time = time.time()

        while time.time() - start_time < 30:

            if cloudflare_process.poll() is not None:
                print(
                    f"{RED}[!] Cloudflare Tunnel stopped unexpectedly."
                    f"{RESET}"
                )
                return False

            line = cloudflare_process.stdout.readline()

            if not line:
                time.sleep(0.1)
                continue

            match = url_pattern.search(line)

            if match:
                cloudflare_url = match.group(0)

                print(
                    f"{GREEN}[+] Cloudflare Tunnel connected.{RESET}"
                )

                print(
                    f"{GREEN}[+] Cloudflare URL:{RESET} "
                    f"{cloudflare_url}"
                )

                return True

        print(
            f"{RED}[!] Could not obtain Cloudflare public URL.{RESET}"
        )

        return False

    except FileNotFoundError:
        print(
            f"{RED}[!] cloudflared was not found.{RESET}"
        )
        print(
            f"{YELLOW}[*] Check: cloudflared --version{RESET}"
        )
        return False

    except Exception as e:
        print(
            f"{RED}[!] Cloudflare error: {e}{RESET}"
        )
        return False


def start_ngrok():
    global ngrok_process
    global ngrok_url

    if ngrok_process is not None and ngrok_url:
        return True

    print(f"{YELLOW}[*] Starting ngrok Tunnel...{RESET}")

    try:
        ngrok_process = subprocess.Popen(
            [
                "ngrok",
                "http",
                "5000"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        url_pattern = re.compile(
            r"https://[a-zA-Z0-9-]+\.ngrok-free\.dev"
        )

        start_time = time.time()

        while time.time() - start_time < 30:

            if ngrok_process.poll() is not None:
                print(
                    f"{RED}[!] ngrok stopped unexpectedly.{RESET}"
                )
                return False

            line = ngrok_process.stdout.readline()

            if not line:
                time.sleep(0.1)
                continue

            match = url_pattern.search(line)

            if match:
                ngrok_url = match.group(0)

                print(
                    f"{GREEN}[+] ngrok Tunnel connected.{RESET}"
                )

                print(
                    f"{GREEN}[+] ngrok URL:{RESET} "
                    f"{ngrok_url}"
                )

                return True

        print(
            f"{RED}[!] Could not obtain ngrok public URL.{RESET}"
        )

        return False

    except FileNotFoundError:
        print(
            f"{RED}[!] ngrok was not found.{RESET}"
        )
        print(
            f"{YELLOW}[*] Check: ngrok version{RESET}"
        )
        return False

    except Exception as e:
        print(
            f"{RED}[!] ngrok error: {e}{RESET}"
        )
        return False


def start_services():
    if not start_flask():
        return False

    if not start_cloudflare():
        stop_services()
        return False

    if not start_ngrok():
        stop_services()
        return False

    return True


def show_training_url(template, path):
    banner()

    print(f"{GREEN}[+] Template : {template}{RESET}")
    print(f"{GREEN}[+] Mode     : Public Security Awareness Training{RESET}")
    print()

    if not start_services():
        pause()
        return

    print(f"{GREEN}[+] Training server : ONLINE{RESET}")
    print(f"{GREEN}[+] Cloudflare      : CONNECTED{RESET}")
    print(f"{GREEN}[+] ngrok           : CONNECTED{RESET}")
    print()

    print(f"{CYAN}[+] Cloudflare Training URL:{RESET}")
    print()
    print(f"    {cloudflare_url + path}")

    print()

    print(f"{CYAN}[+] ngrok Training URL:{RESET}")
    print()
    print(f"    {ngrok_url + path}")

    print()

    print(
        f"{YELLOW}[*] Open the URL manually in your browser.{RESET}"
    )

    print()

    print(
        f"{GREEN}[+] Both URLs route to the {template}"
        f" training page.{RESET}"
    )

    pause()


def stop_process(process):
    if process is None:
        return

    try:
        process.terminate()
        process.wait(timeout=3)

    except Exception:
        try:
            process.kill()
        except Exception:
            pass


def stop_services():
    global flask_process
    global cloudflare_process
    global ngrok_process

    global cloudflare_url
    global ngrok_url

    print()

    if cloudflare_process is not None:
        print(
            f"{YELLOW}[*] Stopping Cloudflare Tunnel...{RESET}"
        )
        stop_process(cloudflare_process)
        cloudflare_process = None

    if ngrok_process is not None:
        print(
            f"{YELLOW}[*] Stopping ngrok Tunnel...{RESET}"
        )
        stop_process(ngrok_process)
        ngrok_process = None

    if flask_process is not None:
        print(
            f"{YELLOW}[*] Stopping Flask server...{RESET}"
        )
        stop_process(flask_process)
        flask_process = None

    cloudflare_url = None
    ngrok_url = None

    print(
        f"{GREEN}[+] All services stopped.{RESET}"
    )


def exit_program():
    banner()

    print(
        f"{YELLOW}[*] Stopping services...{RESET}"
    )

    stop_services()

    print()
    print(
        f"{GREEN}[+] Thank you for using Sociophisher.{RESET}"
    )

    print(
        f"{CYAN}[+] Training session ended.{RESET}"
    )

    sys.exit(0)


def template_menu():

    while True:

        banner()

        print(
            f"{CYAN}[::] Select A Training Template [::]{RESET}\n"
        )

        for key, value in TEMPLATES.items():
            print(
                f"{GREEN}[{key}]{RESET} {value[0]}"
            )

        print()
        print(
            f"{YELLOW}[99]{RESET} About"
        )

        print(
            f"{RED}[00]{RESET} Exit"
        )

        choice = input(
            f"\n{YELLOW}Sociophisher > {RESET}"
        ).strip()

        if choice in TEMPLATES:

            template, path = TEMPLATES[choice]

            show_training_url(
                template,
                path
            )

        elif choice == "99":

            about()

        elif choice == "00":

            exit_program()

        else:

            print(
                f"{RED}[!] Invalid option.{RESET}"
            )

            pause()


def handle_exit_signal(signum, frame):
    print()
    print(
        f"{YELLOW}[*] Shutdown signal received.{RESET}"
    )

    stop_services()

    sys.exit(0)


signal.signal(
    signal.SIGINT,
    handle_exit_signal
)

signal.signal(
    signal.SIGTERM,
    handle_exit_signal
)


if __name__ == "__main__":

    try:
        template_menu()

    except KeyboardInterrupt:

        print()
        print(
            f"{YELLOW}[*] Interrupted by user.{RESET}"
        )

        stop_services()

        print(
            f"{GREEN}[+] Services stopped.{RESET}"
        )

