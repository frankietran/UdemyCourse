def merge_dict(ori, new):
    """
    Function used to merge two dictionary
    Reference source: https://stackoverflow.com/questions/7204805/how-to-merge-dictionaries-of-dictionaries
    :param ori: the data dictionary
    :param new: the modify_data dictionary
    :return: none
    """
    for key in new:
        if key not in ori:
            ori[key] = new[key]
        else:
            if type(ori[key]) == type(new[key]):
                if ori[key] == new[key]:
                    pass
                elif isinstance(ori[key], dict):
                    merge_dict(ori[key], new[key])
                else:
                    ori[key] = new[key]
            else:
                print("Type Err")


if __name__ == "__main__":
    #test mergeDict
    print("ye")
