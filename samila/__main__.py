# -*- coding: utf-8 -*-
"""Samila main."""

import argparse
import matplotlib.pyplot as plt

from art import tprint
from .params import SAMILA_VERSION, GenerateMode, Projection, Marker
from .functions import samila_help
from .genimage import GenerativeImage


def main():
    """
    CLI main function.

    :return: None
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', help='version', action='store_true', default=False)

    parser.add_argument('--load-config', help='load config', type=str)
    parser.add_argument('--load-data', help='load data', type=str)
    parser.add_argument('--function1', help='function1', type=str)
    parser.add_argument('--function2', help='function2', type=str)
    parser.add_argument('--function_seed', help='function seed', type=str)

    parser.add_argument('--seed', help='seed', type=str)
    parser.add_argument('--start', help='start', type=float)
    parser.add_argument('--step', help='step', type=float)
    parser.add_argument('--stop', help='stop', type=float)
    parser.add_argument(
        '--mode',
        help='generation mode',
        type=str,
        choices=[x.value for x in GenerateMode])

    parser.add_argument('--color', help='color', type=str)
    parser.add_argument('--bgcolor', help='bgcolor', type=str)
    parser.add_argument('--cmap', help='cmap', type=str)
    parser.add_argument('--spot-size', help='spot size', type=float)
    parser.add_argument('--size', help='size', type=tuple)
    parser.add_argument('--alpha', help='alpha', type=float)
    parser.add_argument('--linewidth', help='linewidth', type=float)
    parser.add_argument('--rotation', help='rotation', type=float)
    parser.add_argument(
        '--projection',
        help='projection type',
        type=str,
        choices=[x.value for x in Projection])
    parser.add_argument(
        '--marker',
        help='marker type',
        type=str,
        choices=[x.value for x in Marker])

    parser.add_argument('--save-image', help='save image', type=str)
    parser.add_argument('--depth', help='depth', type=float)
    parser.add_argument('--save-data', help='save data', type=str)
    parser.add_argument('--save-config', help='save config', type=str)
    args = parser.parse_args()

    if args.version:
        tprint("samila")
        tprint("V:" + SAMILA_VERSION)
        samila_help()
    else:
        gi = GenerativeImage(
            function1=args.function1,
            function2=args.function2,
            func_seed=args.function_seed,
            data=args.load_data,
            config=args.load_config,
        )
        gi.generate(
            seed=args.seed,
            start=args.start,
            step=args.step,
            stop=args.stop,
            mode=args.mode,
        )
        gi.plot(
            color=args.color,
            bgcolor=args.bgcolor,
            cmap=args.cmap,
            spot_size=args.spot_size,
            size=args.size,
            projection=args.projection,
            marker=args.marker,
            alpha=args.alpha,
            linewidth=args.linewidth,
            rotation=args.rotation,
        )
        plt.show()

        if args.save_image:
            gi.save_image(args.save_image, args.depth)
        if args.save_data:
            gi.save_data(args.save_data)
        if args.save_config:
            gi.save_config(args.save_config)


if __name__ == "__main__":
    main()
