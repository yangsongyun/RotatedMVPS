# 形状评测

## 合成数据（与配置中的合成场景一致）

准备预测网格与评测用参考（路径按你本地的 `configs` 与导出结果调整），例如：

```
data/GlossySynthetic/<object>/
data/meshes/<object>_shape-300000.ply
```

运行 Chamfer 距离（示例对象名 `bell`）：

```shell
python eval_synthetic_shape.py --object bell --mesh data/meshes/bell_shape-300000.ply
```

## 真实数据

1. 在 MeshLab 等工具中清理非物体网格，导出网格。  
2. 在 CloudCompare 等对「预测网格」与「GT 网格」分别采样点云（例如各约 50 万点）。  
3. 将点云保存为例如 `data/point_cloud/<name>-pr.ply` 与 `data/point_cloud/<name>-gt.ply`。  

```shell
python eval_real_shape.py --pr data/point_cloud/bear-pr.ply --gt data/point_cloud/bear-gt.ply
```

---

评测脚本参数以 `--help` 为准；GT 与采样点云需自行准备或与数据集发布方获取。
