''' Grab info from terminal. Clean input before trying to run the rest of the script '''
import sys
# import getopt  # change to argparse
from typing import Optional, Tuple, Dict, List
from datetime import datetime
VERSION = "1.0"

def supported_styles(link: Optional[str] = None) -> None:
    ''' shows supported url styles in terminal '''
    if link:
        print(f'Error: link style not supported\n\t{link}\n')
    print("\nSupported YouTube Link Styles:")
    print("\thttps://www.youtube.com/")
    print("\thttps://www.youtube.com/results?search_query=valuetainment")
    print("\thttps://www.youtube.com/user/patrickbetdavid")
    print("\thttps://www.youtube.com/channel/UCGX7nGXpz-CmO_Arg-cgJ7A")
    print("\thttps://www.youtube.com/watch?v=Z2UmjJ2zQkg&list=PLFa0bDwXvBlDGFtce9u__1sBj6fgi21BE")
    print("\thttps://www.youtube.com/watch?v=x9dgZQsjR6s")
    print('\thttps://www.youtube.com/playlist?list=PLFa0bDwXvBlDGFtce9u__1sBj6fgi21BE')

def usage() -> None:
    ''' show usage information in terminal '''
    print("Works with: YouTube Homepage, youtube search, channel/user, video, and playlists")
    print(f"\n\nUsage: {sys.argv[0]} [OPTIONS]")
    print("\t--link		 \tYouTube link")
    print("\t--api	 	\tGoogle/YouTube API key")
    print("\t--channel      \tYouTube channel name")
    print("\t--comments		Get comments from YouTube videos")
    print("\t\t\t\t   [turning on will increase program run time]")
    print("\t--subtitles		Get subtitles from YouTube videos")
    print("\t--durationseconds	Get seconds from YouTube video duration")
    print("\t--version       \tList version release")
    print("\t--help          \tThis help menu\n")

    print("Example:")
    # print(f"\t{sys.argv[0]} --link [youtube_link] --api [your_api_key] --comments --subtitles --durationseconds")
    print(f"\t{sys.argv[0]} --link [youtube_link] --api [your_api_key] --channel [channel_name] --comments --subtitles --durationseconds --start_date [start_date] --end_date [end_date]")

    supported_styles()
    sys.exit(1)

import argparse
from datetime import datetime
from typing import Tuple, Dict, List

# def get_commands() -> Tuple[str, str,str,str ,str,Dict[str, bool]]:
#     ''' get arguments from command line and parse them '''

#     youtube_link: str = ''
#     api_key: str = ''
#     channel_name: str = ''
#     start_date:str= ''
#     end_date:str= ''
#     comments_on: bool = False
#     subtitiles_on: bool = False
#     seconds_on: bool = False
#     args_values: List[str] = ["link=", "api=", "channel_name=","comments", "subtitles", "durationseconds", "start_date=","end_date=","help", "version"]

#     try:
#         opts, _ = getopt.getopt(sys.argv[1:], "l:n:a:csdhv", args_values)
#     except getopt.GetoptError as err: # print help information and exit:
#         print(err) # will print something like "option -a not recognized"
#         sys.exit(-1)

#     for option, value in opts:
#         if option in ("-l", "--link"):
#             youtube_link = value
#         elif option in ("-a", "--api"):
#             api_key = value
#         elif option in ("-channel", "--channel_name"):  # Added this block
#             channel_name = value    
#         elif option in ("-c", "--comments"):
#             comments_on = True
#         elif option in ("-s", "--subtitles"):
#             subtitiles_on = True
#         elif option in ("-d", "--durationseconds"):
#             seconds_on = True
#         elif option == "--start_date":
#             start_date =datetime.strptime(value,'%Y-%m-%dT%H:%M:%SZ').date() 
#         elif option == "--end_date":
#             end_date = datetime.strptime(value,'%Y-%m-%dT%H:%M:%SZ').date()
#         elif option in ("-h", "--help"):
#             usage()
#             sys.exit()
#         elif option in ("-V", "--version"):
#             print(VERSION)
#             sys.exit(0)
#         else:
#             assert False, "unhandled option"
#             sys.exit(-1)

#     # if not api_key or not youtube_link or 'www.youtube.com' not in youtube_link:
#     if not api_key or not channel_name:
#         usage()
#     options = {'cmtOn': comments_on, 'subOn': subtitiles_on, 'secOn': seconds_on}
#     # youtube_link: str = f'https://www.youtube.com/@{channel_name}/videos'

#     return youtube_link, api_key, options,channel_name, start_date, end_date

def get_commands() -> Tuple[str, str, str, str, str, Dict[str, bool]]:
    parser = argparse.ArgumentParser(description='Your script description')

    parser.add_argument('-l', '--link', help='YouTube link')
    parser.add_argument('-a', '--api', help='API key')
    parser.add_argument('-n', '--channel_name', help='Channel name')
    parser.add_argument('-c', '--comments', action='store_true', help='Include comments')
    parser.add_argument('-s', '--subtitles', action='store_true', help='Include subtitles')
    parser.add_argument('-d', '--durationseconds', action='store_true', help='Include duration in seconds')
    parser.add_argument('--date',  help='date')
   

    args = parser.parse_args()

    youtube_link = args.link
    api_key = args.api
    channel_name = args.channel_name
    comments_on = args.comments
    subtitles_on = args.subtitles
    seconds_on = args.durationseconds
    date = args.date
 
    options = {'cmtOn': comments_on, 'subOn': subtitles_on, 'secOn': seconds_on}

    if not api_key or not channel_name:
        parser.print_help()
        exit()

    return youtube_link, api_key, options, channel_name, date

