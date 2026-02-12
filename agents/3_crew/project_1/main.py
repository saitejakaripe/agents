from crew.project_1.crew import CricketersCrew

if __name__ == "__main__":
    crew = CricketersCrew().crew()
    result = crew.kickoff(inputs={"recipient": "Dear CEO"})
    print("\n\n===== BEST EMAIL =====\n")
    print(result)
