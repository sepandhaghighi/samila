# -*- coding: utf-8 -*-
"""Samila CLI."""
from typing import Dict, List, Any
import time
import argparse
import matplotlib.pyplot as plt
from art import tprint
from .params import SAMILA_VERSION, GenerateMode, Projection, Marker
from .params import LOG_GI_CREATED, LOG_GI_GENERATED, LOG_GI_PLOTTED
from .params import LOG_IMG_SAVED, LOG_DATA_SAVED, LOG_CONFIG_SAVED
from .params import ERR_IMG_SAVE_FAILED, ERR_DATA_SAVE_FAILED, ERR_CONFIG_SAVE_FAILED
from .params import ERR_GENERAL, EXIT_MESSAGE
from .functions import samila_help, print_line
from .genimage import GenerativeImage


def init_argparse() -> argparse.ArgumentParser:
    """Initialize argparse."""
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', help='version', action='store_true', default=False)
    parser.add_argument('--info', help='info', action='store_true', default=False)
    parser.add_argument('--verbose', help='verbose', action='store_true', default=False)

    parser.add_argument('--load-config', help='load config', type=str)
    parser.add_argument('--load-data', help='load data', type=str)
    parser.add_argument('--function1', help='function1', type=str)
    parser.add_argument('--function2', help='function2', type=str)
    parser.add_argument('--function-seed', help='function seed', type=str)

    parser.add_argument('--seed', help='generate seed', type=str)
    parser.add_argument('--start', help='start point', type=float)
    parser.add_argument('--step', help='step size', type=float)
    parser.add_argument('--stop', help='stop point', type=float)
    parser.add_argument(
        '--mode',
        help='generation mode',
        type=str,
        choices=[x.value for x in GenerateMode],
        default=GenerateMode.DEFAULT.value)

    parser.add_argument('--color', help='color', type=str)
    parser.add_argument('--bgcolor', help='background color', type=str)
    parser.add_argument('--cmap', help='cmap', type=str)
    parser.add_argument('--spot-size', help='spot size', type=float)
    parser.add_argument('--size', help='size', type=tuple)
    parser.add_argument('--alpha', help='alpha', type=float)
    parser.add_argument('--linewidth', help='line width', type=float)
    parser.add_argument('--rotation', help='rotation', type=float)
    parser.add_argument(
        '--projection',
        help='projection type',
        type=str,
        choices=[x.value for x in Projection],
        default=Projection.DEFAULT.value)
    parser.add_argument(
        '--marker',
        help='marker type',
        type=str,
        choices=[x.value for x in Marker],
        default=Marker.DEFAULT.value)

    parser.add_argument('--save-image', help='save image', type=str)
    parser.add_argument('--depth', help='depth', type=float)
    parser.add_argument('--save-data', help='save data', type=str)
    parser.add_argument('--save-config', help='save config', type=str)
    parser.add_argument('--no-display', help='no display', action='store_true', default=False)

    return parser


def log_results(is_verbose: bool, result: Dict[str, Any], log_success: str, log_fail: str) -> None:
    """
    Save result function.

    :param is_verbose: is verbose
    :param result: result dictionary
    :param log_success: log for successful result
    :param log_fail: log for failed result
    """
    if is_verbose:
        if result['status']:
            print(log_success.format(result['message']))
            print_line()
        else:
            print(log_fail.format(result['message']))
            print_line()


def run_samila(args: argparse.Namespace) -> None:
    """
    Run samila.

    :param args: arguments
    """
    start_time = time.time()
    projection = Projection(args.projection)
    marker = Marker(args.marker)
    gen_mode = GenerateMode(args.mode)
    gi = GenerativeImage(
        function1=args.function1, function2=args.function2,
        func_seed=args.function_seed, data=args.load_data, config=args.load_config,
    )
    if args.verbose:
        print(LOG_GI_CREATED)
        print_line()
    gi.generate(
        seed=args.seed,
        start=args.start, step=args.step, stop=args.stop,
        mode=gen_mode,
    )
    if args.verbose:
        print(LOG_GI_GENERATED)
        print_line()
    gi.plot(
        color=args.color, bgcolor=args.bgcolor, cmap=args.cmap, spot_size=args.spot_size,
        size=args.size, projection=projection, marker=marker, alpha=args.alpha,
        linewidth=args.linewidth, rotation=args.rotation,
    )
    if args.verbose:
        print(LOG_GI_PLOTTED)
        print_line()
    plt_show_start = time.time()
    if not args.no_display:
        plt.show()
    plt_show_end = time.time()
    if args.save_image:
        result = gi.save_image(args.save_image, args.depth)
        log_results(args.verbose, result, LOG_IMG_SAVED, ERR_IMG_SAVE_FAILED)
    if args.save_data:
        result = gi.save_data(args.save_data)
        log_results(args.verbose, result, LOG_DATA_SAVED, ERR_DATA_SAVE_FAILED)
    if args.save_config:
        result = gi.save_config(args.save_config)
        log_results(args.verbose, result, LOG_CONFIG_SAVED, ERR_CONFIG_SAVE_FAILED)
    end_time = time.time()
    elapsed_time = (end_time - start_time) - (plt_show_end - plt_show_start)
    if args.verbose:
        print("Elapsed time: {0} s".format(round(elapsed_time, 4)))


def main(sys_args: List[Any] = None) -> None:
    """
    CLI main function.

    :param sys_args: system arguments
    """
    parser = init_argparse()
    args = parser.parse_args(args=sys_args)

    if args.version:
        print(SAMILA_VERSION)
    elif args.info:
        tprint("samila")
        tprint("V:" + SAMILA_VERSION)
        samila_help()
    else:
        try:
            run_samila(args=args)
        except (KeyboardInterrupt, EOFError):
            print(EXIT_MESSAGE)
        except Exception as e:
            print(ERR_GENERAL.format(str(e)))
