from faker import Faker

def generate_fake_profiles(num_profiles=10):
    faker = Faker()
    profiles = []

    for _ in range(num_profiles):
        profile = {
            "full_name": faker.name(),
            "email": faker.email(),
            "job_title": faker.job(),
            "company": faker.company(),
        }
        profiles.append(profile)

    return profiles

def print_profiles(profiles):
    for i, profile in enumerate(profiles, start=1):
        print(f"Profile {i}:")
        print(f"  Full Name: {profile['full_name']}")
        print(f"  Email: {profile['email']}")
        print(f"  Job Title: {profile['job_title']}")
        print(f"  Company: {profile['company']}")
        print()  # Print a newline for better readability

def main():
    user_profiles = generate_fake_profiles()
    print_profiles(user_profiles)

if __name__ == "__main__":
    main()
