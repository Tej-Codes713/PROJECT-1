def run_cleanup():

    print("\nResources available for cleanup:\n")

    print("vol-12345")
    print("vol-67890")

    choice = input("\nDo you want to continue? (y/n): ")

    if choice.lower() == "y":
        print("\nCleanup completed successfully!")
    else:
        print("\nCleanup cancelled.")