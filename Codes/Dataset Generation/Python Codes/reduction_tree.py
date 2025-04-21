from compressors_rachana import *
from pp_gen import *

# ************* Single Row Reduction module exact *************** #

def exact_first_stage_single_row_reduction(pp_row,cin1,cin2):
    [sum52,carry52,cout1,cout2]=exact_52(pp_row[3],pp_row[4],pp_row[5],pp_row[6],pp_row[7],cin1,cin2)
    [carry32,sum32]=FA(pp_row[0],pp_row[1],pp_row[2])

    return [sum52,carry52,carry32,sum32,cout1,cout2]

# ************* Single Row Reduction module positive *************** #

def pos_first_stage_single_row_reduction(pp_row):
    [sum52,carry52]=pos_52(pp_row[7],pp_row[6],pp_row[5],pp_row[4],pp_row[3])
    [carry32,sum32]=FA(pp_row[0],pp_row[1],pp_row[2])

    return [sum52,carry52,carry32,sum32]

# ************* Single Row Reduction module negative *************** #

def neg_first_stage_single_row_reduction(pp_row):
    [sum52,carry52]=neg_52(pp_row[7],pp_row[6],pp_row[5],pp_row[4],pp_row[3])
    [carry32,sum32]=FA(pp_row[0],pp_row[1],pp_row[2])

    return [sum52,carry52,carry32,sum32]

# ***************** Binary to decimal conversion ******************* #

def B2Dconversion(pp1,pp2):
    
    res=[0 for i in range(16)]
    carry=[0 for i in range(17)]

    for i in range(16):
        [carry[i+1],res[i]]=FA(pp1[i],pp2[i],carry[i])
    
    pp1.reverse()
    pp2.reverse()
    res.reverse()

    # print("pp1 : ",pp1)
    # print("pp2 : ",pp2[1:17])
    # print("res : ",res)

    spp1 = [str(x) for x in pp1]
    spp2 = [str(x) for x in pp2[1:17]]
    sppres = [str(x) for x in res]
    
    # print("spp1 : ",spp1)
    # print("spp2 : ",spp2)
    # print("sppres : ",sppres)

    jpp1 = int("".join(spp1))
    jpp2 = int("".join(spp2))
    jppres = int("".join(sppres))
    
    # print("jpp1 : ",jpp1)
    # print("jpp2 : ",jpp2)
    # print("jppres : ",jppres)
    
    # sjpp2=jpp2<<1

    # print("sjpp2 : ",sjpp2)
    
    rpp1=str(jpp1)
    rpp2=str(jpp2)
    rppres=str(jppres)
    
    # print("rpp1 : ",rpp1)
    # print("rpp2 : ",rpp2)
    # print("rppres : ",rppres)

    if pp1[0]==1:
        cpp1=findTwoscomplement(rpp1)
        dpp1 = int(cpp1, 2)
        dpp1=dpp1*(-1)
        #print("cpp1 : ",cpp1)
    else :
        cpp1=rpp1
        dpp1 = int(cpp1, 2)
       # print("cpp1 : ",cpp1)
    
    if pp2[1]==1:
        cpp2=findTwoscomplement(rpp2)
        dpp2 = int(cpp2, 2)
        dpp2=dpp2*(-1)
      #  print("cpp2 : ",cpp2)
    else:
        cpp2=rpp2
        dpp2 = int(cpp2, 2)
     #   print("cpp2 : ",cpp2)
    
    if res[0]==1:
        cppres=findTwoscomplement(rppres)
        dppres = int(cppres, 2)
        dppres=dppres*(-1)
      #  print("cpp2 : ",cpp2)
    else:
        cppres=rppres
        dppres = int(cppres, 2)
     #   print("cpp2 : ",cpp2)
    

    # print("decimal pp1 : ", dpp1)
    # print("decimal pp2 : ", dpp2)
    # print("decimal ppres : ", dppres)
    
    return [dpp1,dpp2,dppres]
