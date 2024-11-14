import nltk

# CORPUS = ''.join(nltk.corpus.brown.words())[:1000]
CORPUS = open('corpus/output.txt', 'r', encoding='utf-8').read().replace('’', '')[:100000]

from keyboard import colemak, qwerty, Layout
import pickle

# qwerty.set_fitness(CORPUS)
# print(qwerty.fitness)

colemak.set_fitness(CORPUS)
print(colemak.fitness)

CORPUS = open('corpus/output.txt', 'r', encoding='utf-8').read()[:1000]
colemak.set_fitness(CORPUS)
print(colemak.fitness)

with open('keyboards/keyboard.pkl', 'rb') as f:
	keyboard = pickle.load(f)

# print(keyboard.translate('The quick brown fox jumps over the lazy dog.', colemak))
print(keyboard.translate(r"""importmatplotlib.pyplotaspltfrompointsimportread_pointsfromvisualizeimportplot_circles_and_pointsCIRCLE=50POINT=1RADIUS_DEGREE=3classCircle:def__init__(self,x,y,r):self.x=xself.y=yself.r=rdef__repr__(self):returnf'({self.x},{self.y})|{self.r}'def__contains__(self,point):x,y=pointreturn(x-self.x)**2+(y-self.y)**2<=self.r**2@propertydefcost(self):returnself.r**RADIUS_DEGREE+CIRCLEdefread_circles(file:str):withopen(file)asf:lines=f.readlines()circles=[Circle(*map(float,line.split()))forlineinlines]returncirclesdefvalid_point(point:tuple,circles:list)->bool:forcircleincircles:ifpointincircle:returnTruereturnFalsedefscore(circles:list,points:list)->int:total=0forpointinpoints:ifvalid_point(point,circles):total+=POINTforcircleincircles:total-=circle.costreturntotalif__name__=='__main__':circles=read_circles('circles.txt')points=read_points('points.txt')#print(score(circles,points))fig,ax=plot_circles_and_points(circles,points)plt.show()importPagefrom'@/components/Page';//importSidebar,{SidebarItem}from'@/components/Sidebar';import{faBarChart}from'@fortawesome/free-solid-svg-icons';import{Sidebar,Menu,MenuItem,SubMenu}from'react-pro-sidebar';constFinance=()=>{return(<Pagedata_cluster='Finance'cluster='finance'/>);};exportdefaultFinance;importrandomfromkeyboardimportLayoutimportnltkfromconcurrent.futuresimportThreadPoolExecutorPOPULATION_SIZE=20GENERATIONS=2000MUTATION_RATE=0.2CORPUS=''.join(nltk.corpus.brown.words())[:1000]#CORPUS=open('corpus/output.txt','r',encoding='utf-8').read()[:1000]KEEP_RATE=0.5population=[Layout()for_inrange(POPULATION_SIZE)]#forgenerationinrange(GENERATIONS):static=0previous_fitness=float('-inf')generation=0while(static<1000):#""", colemak))
