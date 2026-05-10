# RotatedMVPS

**Multi-view Photometric Stereo with Rotated Natural Light**

在自然光照与旋转采集条件下，从多视角图像联合恢复物体几何与反射属性的研究与实验代码。

**论文：** IEEE ICME 2025（已录用）· [arXiv:2508.04366](https://arxiv.org/abs/2508.04366)

Teaser 图：[assets/teaser_words.pdf](assets/teaser_words.pdf)

---

## 仓库结构

| 目录 | 说明 |
|------|------|
| `configs/` | 训练、实验与数据配置 |
| `dataset/` | 数据库类型与样本构建 |
| `network/` | 体渲染、场网络与损失相关模块 |
| `train/` | 训练循环、学习率与验证 |
| `utils/` | 通用工具与数据读写 |
| `colmap/` | COLMAP 相关脚本 |
| `blender_backend/` | 与 Blender 配合的重光照等 |
| `raytracing/` | 光线追踪扩展（需按环境编译） |
| `assets/` | 图示资源 |

入口脚本包括：`run_training.py`（训练）、`extract_mesh.py` / `extract_materials.py`（导出）、`relight.py`（重光照）、`run_colmap.py`（位姿与稀疏重建）等。

---

## 文档

- [自定义物体数据准备与流程](custom_object.md)  
- [形状评测（Chamfer 等）](eval.md)

---

## 环境依赖与安装

以下顺序与对外部库的描述方式对齐 [NeRO 仓库](https://github.com/liuyuan-pal/NeRO) 的 **Setup** 说明；**具体命令、CUDA / PyTorch 版本请以各项目当前文档为准**。

### 1. Python 依赖

```bash
pip install -r requirements.txt
```

需本机已安装与 PyTorch 匹配的 **CUDA 工具链**。

### 2. nvdiffrast

按 NVIDIA 官方安装指引安装 **nvdiffrast**（可微光栅化）：

[https://nvlabs.github.io/nvdiffrast/#installation](https://nvlabs.github.io/nvdiffrast/#installation)

### 3. raytracing（可微光线追踪扩展）

NeRO 使用 [ashawkey/raytracing](https://github.com/ashawkey/raytracing) 提供的扩展。本仓库内已包含与上游对应的 `raytracing/` 源码目录，请在**本仓库根目录**下按该项目的说明完成编译与安装，使 Python 能正常 `import` 该模块。

项目主页与说明：[https://github.com/ashawkey/raytracing](https://github.com/ashawkey/raytracing)

### 4. tiny-cuda-nn（可选）

[NeRO 上游仓库](https://github.com/liuyuan-pal/NeRO) 的完整代码树中常带有 `tiny-cuda-nn` 子模块以加速部分隐式网络。**本仓库为减小体积未提交该目录**；且当前主线 Python 代码**未** `import tinycudann`。若你自行对齐上游、或本地仍习惯与 NeRO 相同目录布局，可从 [NVlabs/tiny-cuda-nn](https://github.com/NVlabs/tiny-cuda-nn) 获取源码，按官方 README 编译安装 PyTorch bindings（例如将仓库置于根目录 `tiny-cuda-nn/` 后在 `bindings/torch` 侧安装）。

### 5. 其它

- **COLMAP**、**Blender**：使用 `run_colmap.py`、`relight.py` 时需自行安装并在命令行中指定路径。  
- 训练数据路径、阶段与超参以 `configs/` 下 yaml 为准。

---



## 引用

```bibtex
@inproceedings{yang2025rotatedmvps,
  title     = {RotatedMVPS: Multi-view Photometric Stereo with Rotated Natural Light},
  author    = {Yang, Songyun and Han, Yufei and Zhang, Jilong and Liang, Kongming and Yu, Peng and Qu, Zhaowei and Guo, Heng},
  booktitle = {Proc. {IEEE} Int. Conf. Multimedia and Expo (ICME)},
  year      = {2025},
  address   = {Nantes, France},
  note      = {arXiv:2508.04366}
}
```

---

## 致谢

本仓库在公开可用的神经隐式表面 / 逆渲染实现基础上改进与扩展；其中几何与材质管线受益于社区已有工作，向相关开源作者致谢。
