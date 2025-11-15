import instaloader
import os

L = instaloader.Instaloader()

# Session file (to avoid login every time)
SESSION_FILE = "session_instagram"


def login():
    username = input("Enter Instagram username: ").strip()
    password = input("Enter Instagram password: ").strip()

    try:
        print("[*] Logging in...")

        L.login(username, password)

        # Save session
        L.save_session_to_file(SESSION_FILE)

        print("[✔] Login successful!")
        return True

    except instaloader.exceptions.BadCredentialsException:
        print("[❌] Incorrect username or password.")
    except instaloader.exceptions.TwoFactorAuthRequiredException:
        print("[*] Two-Factor Authentication required.")
        code = input("Enter 2FA code: ").strip()

        try:
            L.two_factor_login(code)
            L.save_session_to_file(SESSION_FILE)
            print("[✔] Login successful with 2FA!")
            return True
        except:
            print("[❌] 2FA verification failed.")

    return False


# --------------------------------
# Load previously saved session
# --------------------------------
def load_old_session():
    try:
        if os.path.exists(SESSION_FILE):
            L.load_session_from_file(username=None, filename=SESSION_FILE)
            print("[✔] Loaded existing session.")
            return True
    except:
        pass

    return False


# --------------------------------
# Download Instagram Post
# --------------------------------
def download_post(url):
    try:
        shortcode = url.rstrip("/").split("/")[-1]
        post = instaloader.Post.from_shortcode(L.context, shortcode)

        folder = f"downloads/{post.owner_username}"
        os.makedirs(folder, exist_ok=True)

        L.download_post(post, target=folder)

        print(f"[✔] Download complete → {folder}")

    except Exception as e:
        print("[❌] Failed to download:", e)


# --------------------------------
# MAIN PROGRAM
# --------------------------------
def main():
    print("=== Instagram Downloader (Login Mode) ===")

    if not load_old_session():
        print("[*] No saved session found. Logging in...")
        if not login():
            return

    print("\nReady to download posts. Enter Instagram URLs below.")
    print("Type 'exit' to quit.\n")

    while True:
        url = input("📥 URL: ").strip()
        if url.lower() == "exit":
            break
        download_post(url)


if __name__ == "__main__":
    main()
