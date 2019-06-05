def time_converter(time):
    new_time = []
    time_split = time.split(":")
    if int(time_split[0]) == 0:
        new_time.append("12")
        new_time.append(":")
        new_time.append(time_split[1])
        new_time.append(" a.m.")
        return "".join(new_time)
    if int(time_split[0]) <= 11:
        new_time.append(str(int(time_split[0])))
        new_time.append(":")
        new_time.append(time_split[1])
        new_time.append(" a.m.")
        return "".join(new_time)
    elif int(time_split[0]) == 12:
        new_time.append(time_split[0])
        new_time.append(":")
        new_time.append(time_split[1])
        new_time.append(" p.m.")
        return "".join(new_time)
    elif int(time_split[0]) >= 13:
        converter = {'13':'1', '14':'2', '15':'3', '16':'4', '17':'5', '18':'6', '19':'7', '20':'8', '21':'9', '22':'10', '23':'11'}
        for k in converter:
            if time_split[0] == k:
                time_split[0] = converter[k]
                new_time.append(time_split[0])
                new_time.append(":")
                new_time.append(time_split[1])
                new_time.append(" p.m.")
        return "".join(new_time)
