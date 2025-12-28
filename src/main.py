from agent import run_agent

if __name__ == "__main__":
    print("Welcome to Smart Maintenance AI Agent!")
    issue = input("Describe the maintenance issue: ")
    task = run_agent(issue)
    print("\nSuggested Maintenance Plan:")
    print(task.json(indent=4))
