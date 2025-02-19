import pandas as pd
def dataFrame(exit_file):
    df = pd.read_csv("ventas.csv", names=["ID","Stock","Sold"])
    df2 = pd.read_csv("ventas2.csv", names=["ID","Stock","Sold"])
    df_concat = pd.concat([df,df2])
    df_ordered = df_concat.sort_values("ID")
    df_withoutStock = df_ordered.loc[df_ordered["Stock"]-df_ordered["Sold"] == 0, :]
    write(exit_file,df_withoutStock)

def write(exit_file,df_withoutStock):
    exit_file.write(f"Elements without stock\n")
    for id in df_withoutStock["ID"]:
        exit_file.write(f"{id} \n")
def main():
    exit_file = open("exit_file.csv","w")
    dataFrame(exit_file)
    exit_file.close()
main()