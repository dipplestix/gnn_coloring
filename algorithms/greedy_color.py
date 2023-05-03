from torch_geometric.utils import to_dense_adj
import random
import torch


def greedy_color(edge_list, shuffle=True):
    # Implemented based on section 3.1 of "Guide to Graph Colouring" - R.M.R. Lewis
    n = torch.max(edge_list) + 1
    colors = [None]*n
    color_map = {0:[]}
    nodes = list(range(n))
    adj = to_dense_adj(edge_list).squeeze(0)
    latest_color = 0
    if shuffle:
        random.shuffle(nodes)
    for node in nodes:
        for color in color_map:
            feasible_color = True
            for colored_node in color_map[color]:
                if adj[node][colored_node] != 0:
                    feasible_color = False
                    break
            if feasible_color:
                color_map[color].append(node)
                colors[node] = color
                break
        else:
            latest_color += 1
            color_map[latest_color] = [node]
            colors[node] = latest_color
    return colors


