from project_profile import generate_project_profile
from billing_engine import generate_billing
from cost_engine import analyze_costs
from summary_view import show_summary

def main():
    while True:
        print("\nAI Cloud Cost Optimizer")
        print("1. Enter project description")
        print("2. Run cost analysis")
        print("3. View summary")
        print("4. Exit")

        choice = input("Choose option: ").strip()

        if choice == "1":
            text = input("\nEnter project description:\n")
            with open("project_input.txt", "w") as f:
                f.write(text)
            print("Project description saved.")

        elif choice == "2":
            with open("project_input.txt") as f:
                description = f.read()

            project = generate_project_profile(description)
            billing = generate_billing(project)
            analyze_costs(project, billing)
            print("Cost analysis completed.")

        elif choice == "3":
            show_summary()

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()