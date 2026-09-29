def create_sample_log():
    logs = [
        "INFO User logged in",
        "SUCCESS File uploaded",
        "WARNING Low disk space",
        "ERROR Database connection failed",
        "INFO User logged out",
        "SUCCESS Payment completed",
        "ERROR File not found",
        "WARNING High memory usage",
        "INFO User logged in",
        "SUCCESS Request completed"
    ]

    with open("system.log", "w") as file:
        for log in logs:
            file.write(log + "\n")


def analyze_log():
    info = 0
    success = 0
    warning = 0
    error = 0

    with open("system.log", "r") as file:
        for line in file:
            if line.startswith("INFO"):
                info += 1
            elif line.startswith("SUCCESS"):
                success += 1
            elif line.startswith("WARNING"):
                warning += 1
            elif line.startswith("ERROR"):
                error += 1

    print("\n========== LOG ANALYSIS ==========")
    print("INFO messages:", info)
    print("SUCCESS messages:", success)
    print("WARNING messages:", warning)
    print("ERROR messages:", error)
    print("Total log entries:", info + success + warning + error)


def main():
    print("========== LOG FILE ANALYZER ==========")

    create_sample_log()

    print("\nSample log file created: system.log")

    analyze_log()


if __name__ == "__main__":
    main()