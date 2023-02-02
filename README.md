# trans_UAV_for_yolov5jde
## Use in yolov5jde

1.download [transformed files](https://pan.baidu.com/s/1g5JLC1OOLLsIsNmRVx43Bg?pwd=s76V) and [UAV-benchmark-M](https://drive.google.com/file/d/1m8KA6oPIRK_Iwt9TYFquC87vBc_8wRVc/view?usp=sharing)

2.rename walk_files_results.txt to uav.train and cut a part as uav.val 

3.put files in yolov5jde project (you need to change the structure of UAV-benchmark-M):

    yolov5jde
        -mot_data
            -UAV-benchmark-M
                -images
                    -M0101
                    -M0201
                    ...
                -labels_with_ids
                    -M0101
                    -M0201
                    ...
            -uav.train
            -uav.val


4.add uav to mot.yaml

    root: <yolov5jde path>\mot_data

    train: {
        uav: ./mot_data/uav.train
        <other datasets>
        }

    test: {
        uav: ./mot_data/uav.val
        <other datasets>
    }


    # number of classes
    nc: 1

    # class names
    names: ['person']


## Run transform by yourself

1.Put origin folder "UAV-benchmark-M" in the root directory of the project. 

2.run ```python walk_files.py```