# 自定义物体：数据准备与重建流程

以下以物体名称 `kettle` 为例，说明从多视角照片到形状、材质与重光照的典型步骤。

## 1. 目录布局

将原始图像置于：

```
data/custom/kettle/images/
```

## 2. COLMAP

在同一相机假设下运行稀疏重建（请将 `<colmap>` 换为本机 COLMAP 可执行文件路径）：

```shell
python run_colmap.py --project_dir data/custom/kettle --colmap <colmap> --same_camera
```

## 3. 物体区域与坐标

- 用 COLMAP 点云裁出目标物体，导出为 `data/custom/kettle/object_point_cloud.ply`（仅用于界定重建范围，不直接作为监督几何）。
- 编写 `data/custom/kettle/meta_info.txt`：第一行为 **Z+（up）** 方向，第二行为 **X+（forward）** 方向（与处理脚本约定一致）。

## 4. 训练与导出

确认 `data/custom/kettle/` 下已有 `images/`、`colmap/`、`object_point_cloud.ply`、`meta_info.txt` 后：

```shell
python run_training.py --cfg configs/custom/kettle_shape.yaml
python extract_mesh.py --cfg configs/custom/kettle_shape.yaml
python run_training.py --cfg configs/custom/kettle_material.yaml
python extract_materials.py --cfg configs/custom/kettle_material.yaml
```

网格与材质默认写入 `data/meshes/`、`data/materials/`（具体文件名与步数见配置）。

## 5. 重光照

```shell
python relight.py --blender <blender可执行文件> \
  --name kettle-neon \
  --mesh data/meshes/kettle_shape-300000.ply \
  --material data/materials/kettle_material-100000 \
  --hdr data/hdr/neon_photostudio_4k.exr
```

输出目录一般为 `data/relight/<name>/`。

---

示例数据与更多演示资源若需对外发布，请单独提供下载链接或附录说明。
