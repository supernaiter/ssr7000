# SSR7000: A SYNCHRONIZED CORPUS OF ULTRASOUND TONGUE IMAGING FOR END-TO-END SILENT SPEECH RECOGNITION

![raw_compressed](https://user-images.githubusercontent.com/14064383/126605549-ea724b36-f1e5-4731-b031-aa72befe9be0.gif) ![raw2_compressed](https://user-images.githubusercontent.com/14064383/126605564-7d2c0528-cf93-4fa9-bb21-9e3c23de318d.gif) ![raw3_compressed](https://user-images.githubusercontent.com/14064383/126605576-c27ef8b8-cbcb-407d-8af7-d9fad09e964b.gif)

# Overview

The SSR7000 corpus is a recording set of **7384** utterances of training data and 100 utterances of test data by a single male native English speaker. All utterances were recorded with silent speech in which the participant did not speak aloud but only moved his articulatory organs. The recordings of the lip and ultrasound tongue images were synchronized when the speaker was silently speaking. 

Here you can download the dataset and the recipe we used for the benchmark result. The corpus is publicly available under the CC BY-NC4.0 license.

## Downloads

You can download the dataset from [HERE](https://zenodo.org/records/16934924).

The SSR7000 provides both raw data without any preprocessing and the processed data. The raw data is useful for those who wish to work on improving the preprocessing. For those who are more interested in the recognizer rather than in the preprocessing, we have provided the preprocessed data too.

## How to Use the Recipe

1. Install ESPnet (not ESPnet2) following their [instruction](https://github.com/espnet/espnet).

2. Put our recipe folder under espnet/egs, like espnet/egs/**recipe**.

## Google Colab

You can try our benchmark recognition on Google Colab [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/19Ltv3O3yuB81yoUclY5CEbGpALjiDgr1?usp=sharing) without any environment setting!

## Baseline

Our benchmark results using [ESPnet](https://github.com/espnet/espnet) and the recipe on this repository. This table shows a comparison of the number of data.
|   |1000 |3000|5000|7384 (all)|
|---|-----|----|----|----|
|CER|51.5 |47.4|23.7|`17.6`  |
|WER|89.5 |81.0|50.0|`37.6` |      

## Contact

kimura-naoki[at]g.ecc.u-tokyo.ac.jp
