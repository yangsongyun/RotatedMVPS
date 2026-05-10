import argparse

from pathlib import Path
import numpy
import cv2
import torch
import trimesh
import os
from network.renderer import name2renderer
from utils.base_utils import load_cfg


def main():
    cfg = load_cfg(flags.cfg)


    network = name2renderer[cfg['network']](cfg,extract_env=True)
    #使用shape数据集
    #network = name2renderer[cfg['network']](cfg,training=False)
    ckpt = torch.load(f'data/model/{cfg["name"]}/model.pth')
    step = ckpt['step']
    network.load_state_dict(ckpt['network_state_dict'])
    network.eval().cuda()
    torch.set_default_tensor_type('torch.cuda.FloatTensor')
    print(f'successfully load {cfg["name"]} step {step}!')


    with torch.no_grad():
        #lights = network.color_network.env_light(500, 1000)
        lights = network.shader_network.env_light(500, 1000)
        
    light = lights.cpu().numpy()
    print(numpy.shape(light))
    # output geometry
    light=light*255
    output_dir = Path('data/light')
    output_dir.mkdir(exist_ok=True)
    path = os.path.join(output_dir,'{}.png'.format(cfg["name"]))
    cv2.imwrite(path,light)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, required=True)
    parser.add_argument('--resolution', type=int, default=512)
    flags = parser.parse_args()
    main()
