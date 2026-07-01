from app.runner import analyze_company


def main():

    report = analyze_company(

        company="Tesla",

        report_type="Complete Business Report",

    )

    print("\n")
    print("=" * 80)
    print(report)
    print("=" * 80)


if __name__ == "__main__":

    main()