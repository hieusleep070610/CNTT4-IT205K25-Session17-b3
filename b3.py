import itertools

teams_list = []
match_schedule = []


def input_teams():
    global teams_list

    data = input("Nhập các đội (cách nhau bởi dấu phẩy): ")

    teams = [team.strip().upper() for team in data.split(",")]

    unique_teams = []
    seen = set()

    for team in teams:
        if team and team not in seen:
            unique_teams.append(team)
            seen.add(team)

    teams_list = unique_teams

    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")


def create_schedule():
    global match_schedule

    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return

    matches = itertools.combinations(teams_list, 2)

    match_schedule = [f"{team1} vs {team2}" for team1, team2 in matches]

    print("--- LỊCH THI ĐẤU VÒNG BẢNG ---")

    for count, match in enumerate(match_schedule, start=1):
        print(f"{count}. {match}")

    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")


def generate_match_ids():
    if len(match_schedule) == 0:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return

    print("--- MÃ TRẬN ĐẤU (MATCH ID) ---")

    for index, match in enumerate(match_schedule, start=1):
        team1, team2 = match.split(" vs ")

        code1 = team1[:3].ljust(3, "X")
        code2 = team2[:3].ljust(3, "X")

        match_id = f"M{index:02d}-{code1}-{code2}"

        print(f"Trận {index} ({match}) -> ID: {match_id}")


while True:
    print("\n============= ESPORTS MATCHMAKER =============")
    print("1. Nhập danh sách Đội tuyển")
    print("2. Tạo lịch thi đấu (Combinations)")
    print("3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)")
    print("4. Đóng hệ thống")
    print("==============================================")

    choice = input("Chọn chức năng (1-4): ")

    match choice:
        case "1":
            print("--- NHẬP DANH SÁCH ---")
            input_teams()

        case "2":
            create_schedule()

        case "3":
            generate_match_ids()

        case "4":
            print("Đóng hệ thống. Tạm biệt!")
            break

        case _:
            print("Lựa chọn không hợp lệ.")
