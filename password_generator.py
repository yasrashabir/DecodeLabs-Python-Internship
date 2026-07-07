# Project 3: Random Password Generator - DecodeLabs
# By: Yasra Shabir

import secrets
import string
import math

def generate_password(length):
    # PDF ke mutabiq: string module use karo
    characters = string.ascii_letters + string.digits + string.punctuation
    # PDF ke mutabiq: secrets.choice() use karo (NOT random.choice)
    # PDF ke mutabiq: .join() use karo (enterprise approach)
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def calculate_entropy(length, pool_size):
    # PDF mein entropy formula: E = L x log2(R)
    entropy = length * math.log2(pool_size)
    return entropy

def get_strength(entropy):
    if entropy < 40:
        return "❌ Weak"
    elif entropy < 60:
        return "⚠️ Moderate"
    elif entropy < 80:
        return "✅ Strong"
    else:
        return "🔒 Very Strong"

def main():
    print("🔐 Welcome to DecodeLabs Password Generator!\n")
    
    while True:
        print("1. Generate Password")
        print("2. Exit")
        choice = input("\nEnter choice (1/2): ")
        
        if choice == "1":
            try:
                length = int(input("Enter password length (min 8): "))
                if length < 8:
                    print("❌ Minimum length is 8!")
                    continue
                
                password = generate_password(length)
                pool_size = len(string.ascii_letters + string.digits + string.punctuation)
                entropy = calculate_entropy(length, pool_size)
                strength = get_strength(entropy)
                
                print(f"\n🔑 Generated Password: {password}")
                print(f"📊 Entropy: {entropy:.1f} bits")
                print(f"💪 Strength: {strength}\n")
                
            except ValueError:
                print("❌ Invalid! Enter a number.")
                
        elif choice == "2":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()