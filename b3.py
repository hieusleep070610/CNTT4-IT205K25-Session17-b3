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
        if team != "" and team not in seen:
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

    count = 1
    for match in match_schedule:
        print(f"{count}. {match}")
        count += 1

    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")


def generate_match_ids():
    if len(match_schedule) == 0:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return

    print("--- MÃ TRẬN ĐẤU (MATCH ID) ---")

    index = 1

    for match in match_schedule:
        team1, team2 = match.split(" vs ")

        code1 = f"{team1[:3]:X<3}"
        code2 = f"{team2[:3]:X<3}"

        match_id = f"M{index:02d}-{code1}-{code2}"

        print(f"Trận {index} ({match}) -> ID: {match_id}")

        index += 1


while True:
    print("============= ESPORTS MATCHMAKER =============")
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