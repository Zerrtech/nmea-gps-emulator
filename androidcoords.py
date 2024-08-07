coords = [
(-116.21022238975492,43.62317849075733,214.67761,1723053280010,13.888889),
(-116.21032031625593,43.623079683744066,215.75296,1723053281011,13.888889),
(-116.21041504220896,43.62297909281111,214.37582,1723053282011,13.888889),
(-116.21050731414083,43.62288045729773,214.19939,1723053283011,13.888889),
(-116.21060006966967,43.62278130483588,214.19943,1723053284011,13.888889),
(-116.2106915989562,43.62268840104381,215.59152,1723053285012,13.888889),
(-116.21078309387934,43.622597009249965,216.02745,1723053286013,13.888889),
(-116.21087923652495,43.62250407135921,216.9251,1723053287011,13.888889),
(-116.210977136567,43.6224094346519,216.92513,1723053288012,13.888889),
(-116.21107203861128,43.6223176960091,216.92519,1723053289012,13.888889),
(-116.21116535821537,43.62222464178463,216.07451,1723053290012,13.888889),
(-116.21125981983117,43.622130180168824,215.99693,1723053291011,13.888889),
(-116.21135650645266,43.62203349354734,215.99698,1723053292011,13.888889),
(-116.21145076576322,43.62193923423679,215.99702,1723053293012,13.888889),
(-116.21133528271493,43.6218775357466,126.33195,1723053294011,13.888889),
(-116.2112064738922,43.62181024755563,125.71926,1723053295012,13.888889),
(-116.21108004027332,43.62174420014278,125.71924,1723053296013,13.888889),
(-116.21095109204418,43.62167683912755,125.71921,1723053297012,13.888889),
(-116.21082340118733,43.621610134948604,125.71917,1723053298012,13.888889),
(-116.21069473231245,43.62154291986471,125.71914,1723053299012,13.888889),
(-116.2105651122,43.6214775561,124.766106,1723053300013,13.888889),
(-116.21043668045724,43.62141519131432,123.75958,1723053301012,13.888889),
(-116.21030021800834,43.62135010900417,123.28475,1723053302012,13.888889),
(-116.21016825234913,43.621284126174565,124.53803,1723053303012,13.888889),
(-116.21003523576583,43.62121639470415,125.027245,1723053304011,13.888889),
(-116.20990579266187,43.62115040410213,125.05936,1723053305011,13.888889),
(-116.20977846238165,43.621085490625944,125.059326,1723053306011,13.888889),
(-116.2096497217735,43.621019860886754,125.05818,1723053307011,13.888889),
(-116.20951860712431,43.62095430356216,124.53789,1723053308012,13.888889),
(-116.20938777612275,43.62088888806138,124.53786,1723053309011,13.888889),
(-116.20925807913726,43.62082403956863,124.537834,1723053310012,13.888889),
(-116.20912839364561,43.62075639653397,125.67742,1723053311011,13.888889),
(-116.20899703137344,43.6206934057831,123.42723,1723053312011,13.888889),
(-116.208861979717,43.62062473544932,124.988815,1723053313011,13.888889),
(-116.20872819697883,43.62055671032821,124.988785,1723053314011,13.888889),
(-116.20859286360455,43.620487896748074,124.98876,1723053315012,13.888889),
(-116.2084616183765,43.620421161886355,124.988716,1723053316012,13.888889),
(-116.20833217148858,43.62035495973773,125.144485,1723053317012,13.888889),
(-116.20820340399061,43.62028892512339,125.21806,1723053318011,13.888889),
(-116.2080680294401,43.620219502276974,125.21803,1723053319012,13.888889),
(-116.2079300065355,43.62015384917024,123.21492,1723053320012,13.888889),
(-116.20779944672665,43.62008972336332,124.06174,1723053321011,13.888889),
(-116.20766847517353,43.62002423758676,124.537476,1723053322011,13.888889),
(-116.20753892112397,43.61995946056199,124.537445,1723053323012,13.888889),
(-116.2074073827525,43.61989369137625,124.53742,1723053324012,13.888889),
(-116.20727626973235,43.619828134866175,124.53739,1723053325011,13.888889),
(-116.20714544041894,43.61976120466556,125.152695,1723053326012,13.888889),
(-116.20701750493937,43.61969368316245,125.99751,1723053327011,13.888889),
(-116.20688274813475,43.619622561515556,125.99748,1723053328012,13.888889),
(-116.20674702670809,43.61955351335404,125.00287,1723053329012,13.888889),
(-116.20679059806778,43.61946936068616,200.61395,1723053330011,13.888889),
(-116.20688122411809,43.61937248456343,214.20096,1723053331012,13.888889),
(-116.20697088292745,43.619276642387895,214.20099,1723053332012,13.888889),
(-116.20705976798034,43.61918162733137,214.20103,1723053333013,13.888889),
(-116.20715077596489,43.619089224035115,215.58476,1723053334012,13.888889),
(-116.20724290983749,43.618997090162516,215.99835,1723053335012,13.888889),
(-116.20733552247565,43.618903096905434,215.59618,1723053336012,13.888889),
(-116.20742322168374,43.618806778316255,213.48415,1723053337011,13.888889),
]

def get_hst():
    # g = Geod(ellps='WGS84')
    hs = []
    for ci in range(len(coords)-1):
        prev = coords[ci]
        curr = coords[ci+1]

        # print(out)
        # find distace between points
        # find heading between points
        # convert to knots
        speed = prev[4] * 1.943844
        mph = (prev[4] * 0.000621371) * 3600
        time_in_secs = (curr[3] - prev[3]) / 1000
        heading = prev[2]
        # heading = (heading + 360) % 360
        hs.append((heading, speed, time_in_secs))
        print("speed knots:", speed, " mph:", mph, " heading:", heading, " time in sec:", time_in_secs)
    return hs

if __name__ == '__main__':
    get_hst()
