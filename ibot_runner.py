import yaml
from sys import argv
from subprocess import call



def main(args):
    reportListingF = args[0]
    destDir = args[1]
    with open(reportListingF) as rlf:
        reportListings = yaml.load(rlf)
        for name, rl in reportListings.items():
            kind = rl['kind']
            loc = rl['location']
            cmd = 'multiqc -f -m {} -n {}/{}_{}.ibot_report.html {}'.format(kind,kind,name,destDir,loc)  
            print(cmd)
            call(cmd,shell=True)
            


if __name__ == '__main__':
    main(argv[1:])
