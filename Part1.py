from webexteamssdk import WebexTeamsAPI

def get_access_token():
    choice = input("Do you want to use a hard-coded token? (y/n): ")
    if choice.lower() == "n":
        access_token = input("Enter your access token: ").strip()
    else:
        access_token = "OGE0YjFkOWEtNzY1My00NzhjLTg5MTUtNmYyZmEyOTRiZjZlODJhZWUyOTItYTMx_P0A1_60c4241b-f916-4111-96c4-b4c6eecaa22e"
    return access_token

def main():
    access_token = get_access_token()
    api = WebexTeamsAPI(access_token=access_token)

    room_name = input("Enter the name of the room you want to create: ").strip()
    room = api.rooms.create(room_name)
    print(f"Room '{room.title}' created successfully with ID: {room.id}")

    welcome_message = input("Enter the welcome message you want to send: ").strip()
    api.messages.create(room.id, text=welcome_message)
    print("Welcome message sent successfully.")

if __name__ == "__main__":
    main()
