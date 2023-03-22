from awpy.types import GameFrame, GameRound
from typing import Literal, cast
import os
import shutil
from awpy.visualization.plot import position_transform
from awpy.visualization.plot import plot_positions
from tqdm import tqdm
import imageio
import matplotlib.pyplot as plt

def plot_round_deaths(
    filename: str,
    frames: list[GameFrame],
    map_name: str = "de_ancient",
    map_type: str = "original",
    dark: bool = False,
    fps: int = 10,
) -> Literal[True]:
    if os.path.isdir("csgo_tmp"):
        shutil.rmtree("csgo_tmp/")
    os.mkdir("csgo_tmp")
    image_files = []
    for i, f in tqdm(enumerate(frames)):
        positions = []
        colors = []
        markers = []
        # Plot players
        for side in ["ct", "t"]:
            side = cast(Literal["ct", "t"], side)
            for p in f[side]["players"] or []:
                if p["hp"] > 0:
                    continue
                if side == "ct":
                    colors.append("cyan")
                else:
                    colors.append("red")
                markers.append("x")
                pos = (
                    position_transform(map_name, p["x"], "x"),
                    position_transform(map_name, p["y"], "y"),
                )
                positions.append(pos)
        fig, _ = plot_positions(
            positions=positions,
            colors=colors,
            markers=markers,
            map_name=map_name,
            map_type=map_type,
            dark=dark,
        )
        image_files.append(f"csgo_tmp/{i}.png")
        fig.savefig(image_files[-1], dpi=300, bbox_inches="tight")
        plt.close()
    images = []
    for file in image_files:
        images.append(imageio.imread(file))
    imageio.mimsave(filename, images, fps=fps)
    shutil.rmtree("csgo_tmp/")
    return True

def plot_game_deaths_overlay(
    filename: str,
    rounds: list[GameRound],
    map_name: str = "de_ancient",
    map_type: str = "original",
    dark: bool = False,
    fps: int = 10,
) -> Literal[True]:
    if os.path.isdir("csgo_tmp"):
        shutil.rmtree("csgo_tmp/")
    os.mkdir("csgo_tmp")
    image_files = []

    framesLeft = True
    frameIndex = 0
    positions = []
    colors = []
    markers = []
    print(max(len(r["frames"]) for r in rounds))
    while framesLeft:
        framesLeft = False
        for i, r in tqdm(enumerate(rounds)):
            if len(r["frames"]) <= frameIndex:
                continue
            f = r["frames"][frameIndex]
            framesLeft = True
            # Plot players
            for side in ["ct", "t"]:
                side = cast(Literal["ct", "t"], side)
                for p in f[side]["players"] or []:
                    if p["hp"] > 0:
                        continue
                    if side == "ct":
                        colors.append("cyan")
                    else:
                        colors.append("red")
                    markers.append("x")
                    pos = (
                        position_transform(map_name, p["x"], "x"),
                        position_transform(map_name, p["y"], "y"),
                    )
                    positions.append(pos)
        frameIndex += 1
        fig, _ = plot_positions(
            positions=positions,
            colors=colors,
            markers=markers,
            map_name=map_name,
            map_type=map_type,
            dark=dark,
        )
        image_files.append(f"csgo_tmp/{frameIndex}.png")
        fig.savefig(image_files[-1], dpi=300, bbox_inches="tight")
        plt.close()
    images = []
    for file in image_files:
        images.append(imageio.imread(file))
    imageio.mimsave(filename, images, fps=fps)
    shutil.rmtree("csgo_tmp/")
    return True

def plot_game_deaths_overlay_last_frame(
    filename: str,
    rounds: list[GameRound],
    map_name: str = "de_ancient",
    map_type: str = "original",
    dark: bool = False,
    fps: int = 10,
) -> Literal[True]:
    framesLeft = True
    frameIndex = 0
    positions = []
    colors = []
    markers = []
    while framesLeft:
        framesLeft = False
        for i, r in tqdm(enumerate(rounds)):
            if len(r["frames"]) <= frameIndex:
                continue
            f = r["frames"][frameIndex]
            framesLeft = True
            # Plot players
            for side in ["ct", "t"]:
                side = cast(Literal["ct", "t"], side)
                for p in f[side]["players"] or []:
                    if p["hp"] > 0:
                        continue
                    if side == "ct":
                        colors.append("cyan")
                    else:
                        colors.append("red")
                    markers.append("x")
                    pos = (
                        position_transform(map_name, p["x"], "x"),
                        position_transform(map_name, p["y"], "y"),
                    )
                    positions.append(pos)
        frameIndex += 1
    fig, _ = plot_positions(
        positions=positions,
        colors=colors,
        markers=markers,
        map_name=map_name,
        map_type=map_type,
        dark=dark,
    )
    return fig