#!/usr/bin/env python3
import os
import shutil
import sys

if __name__ == "__main__":
    raw_feats_dir = sys.argv[1]

    utts_texts = dict()
    utts_texts["train_utts"] = []
    utts_texts["train_texts"] = []
    utts_texts["train_scps"] = []

    utts_texts["val_utts"] = []
    utts_texts["val_texts"] = []
    utts_texts["val_scps"] = []

    utts_texts["test_utts"] = []
    utts_texts["test_texts"] = []
    utts_texts["test_scps"] = []

    with open(f"{raw_feats_dir}/../train_text","r") as t:
        train_val_text = t.readlines()
        for i in range(len(train_val_text)):
            utt,text = train_val_text[i].split(" ",1)
            if 50 <= i < len(train_val_text) - 50:
                utts_texts["train_utts"].append(utt)
                utts_texts["train_texts"].append(text.strip())
            else:
                utts_texts["val_utts"].append(utt)
                utts_texts["val_texts"].append(text.strip())

    with open(f"{raw_feats_dir}/train.scp","r") as s:
        train_val_scp = s.readlines()
        for i in range(len(train_val_scp)):
            utt,scp = train_val_scp[i].split(" ",1)
            if utt in utts_texts["val_utts"]:
                utts_texts["val_scps"].append(train_val_scp[i])
            else:
                utts_texts["train_scps"].append(train_val_scp[i])

    with open(f"{raw_feats_dir}/../test_text","r") as t:
        test_text = t.readlines()
        for tt in test_text :
            utts_texts["test_utts"].append(tt.split(" ",1)[0])
            utts_texts["test_texts"].append(tt.split(" ",1)[1].strip())

    with open(f"{raw_feats_dir}/test.scp","r") as s:
        utts_texts["test_scps"] = s.readlines()

    for dataset in ["train","val","test"]:

        utts = utts_texts[f"{dataset}_utts"]
        texts = utts_texts[f"{dataset}_texts"]
        scps = utts_texts[f"{dataset}_scps"]

        dataset_dir = f"data/{dataset}"
        n_utts = len(utts)

        spk2utt = "Larry " + " ".join(utts)
        utt2spk = []
        wav = []

        for i in range(n_utts):
            utt2spk.append(utts[i] + " Larry\n")
            wav.append(utts[i] + " " + str(i) + ".wav\n")
        with open(dataset_dir + "/feats.scp", "w") as s:
            s.writelines(scps)
        with open(dataset_dir + "/text", "w") as t:
            for i in range(n_utts):
                t.write(f"{utts[i]} {texts[i]}\n")
        with open(dataset_dir + "/spk2utt", "w") as s:
            s.writelines(spk2utt)
        with open(dataset_dir + "/utt2spk", "w") as u:
            u.writelines(utt2spk)
        with open(dataset_dir + "/wav.scp", "w") as w:
            w.writelines(wav)
        