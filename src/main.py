import src.drive, src.track
from src.drive import *
import plotly.express as px
import pandas

if __name__ == "__main__":
    xStartPos = src.drive.xStartPos
    ySegment = src.drive.ySegment
    lapTime = src.drive.lapTime
    track = src.track.track1

    while ySegment < len(track[0]):
        # print(ySegment)
        xPotential = genXPot(xStartPos)
        # print("xPotential: " + str(xPotential))
        T_temp, xStartPos, V_temp = selectOptimalTime(calcsteptime, xStartPos, xPotential, ySegment, V_list, 500, track)
        print(T_temp)
        # print("T_temp: %s\nxStartPos: %s\nV_temp: %s" % (str(T_temp), str(xStartPos), str(V_temp)))
        # print("xHistory: %s\nxStartPos: %s\nV_list: %s\nV_temp: %s\nlapTime: %s\nT_temp: %s\nySegment: %s"
        #       % (str(xHistory), str(xStartPos), str(V_list), str(V_temp), str(lapTime), str(T_temp), str(ySegment)))
        lapTime, ySegment = increment(xHistory, xStartPos, V_list, V_temp, lapTime, T_temp, ySegment)
        xStartPos = flipTrack(ySegment, xStartPos)
        # print("xHistory: %s\nxStartPos: %s\nV_list: %s\nV_temp: %s\nlapTime: %s\nT_temp: %s\nySegment: %s"
        #       % (str(xHistory), str(xStartPos), str(V_list), str(V_temp), str(lapTime), str(T_temp), str(ySegment)))
    for i in range(len(V_list)):
        V_list[i] = round(V_list[i] * 2.23694, 2)
    print("xHistory: %s\nxStartPos: %s\nV_list: %s\nV_temp: %s\nlapTime: %s\nT_temp: %s\nySegment: %s"
          % (str(xHistory), str(xStartPos), str(V_list), str(V_temp), str(lapTime), str(T_temp), str(ySegment)))

    testVal = [0] * len(V_list)
    for i in range(len(V_list)):
        testVal[i] = i
    fig = px.line(x=testVal, y = V_list, template= "simple_white", markers=True)
    fig.show()
