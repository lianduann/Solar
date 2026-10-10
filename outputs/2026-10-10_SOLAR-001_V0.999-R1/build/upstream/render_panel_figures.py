"""New presentation exhibits from frozen tables and arithmetic summaries. No fitting."""
from pathlib import Path
import pandas as pd, numpy as np, json, hashlib
import chart_theme as T
T.apply()
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
D=Path(__file__).resolve().parents[1]; P=D/'data/panel'; F=D/'figures'
lineage=[]
def save(fig,name,title,inputs,columns,ops,sub=None):
 png,vec=T.finish(fig,F/(name+'.png'),title,sub)
 lineage.append(dict(figure=str(png.relative_to(D)),vector=str(vec.relative_to(D)),inputs=inputs,columns=columns,operation=ops,input_sha256={i:hashlib.sha256((D/i).read_bytes()).hexdigest() for i in inputs},png_sha256=hashlib.sha256(png.read_bytes()).hexdigest()))
fact=json.loads((D/'data/supplement/A/A_summary_facts.json').read_text())
fig,ax=T.newfig(3.0);x=np.linspace(-50,30,81);fac=fact['module_share_mmp']*fact['pass_through_k'];ax.plot(x,x*fac,color=T.NAVY)
for x0 in [-10,-20,-30]:
 ax.plot(x0,x0*fac,'o',color=T.TEAL);ax.annotate(f'{x0}% module\n{x0*fac:.2f}% PV cost',(x0,x0*fac),xytext=(8,-24),textcoords='offset points',fontsize=7)
ax.axhline(0,lw=.6,color=T.AXIS);ax.axvline(0,lw=.6,color=T.AXIS);ax.set(xlabel='Assumed U.S. module-input change (%)',ylabel='PV-only modeled cost change (%)',xlim=(-50,30),ylim=(-17,11))
save(fig,'Panel_Module_Transmission','U.S. module-price sensitivity, other inputs held fixed',['data/supplement/A/A_summary_facts.json'],['module_share_mmp','pass_through_k'],'Multiply assumed percentage by module share and marginal factor','No China-to-U.S. price transmission is estimated')
a=pd.read_csv(P/'Intraday-Net-Load-2025.csv')
fig,ax=T.newfig(3.8)
for col,label,color,ls in [('load_mw','Load',T.NAVY,'-'),('solar_mw','Solar',T.AMBER,'-'),('wind_mw','Wind',T.TEAL,'-'),('net_load_mw','Load less wind and solar',T.BRICK,'--')]:
 ax.plot(a.hour,a[col]/1000,label=label,color=color,ls=ls)
ax.set(xlabel='America/Chicago civil hour starting',ylabel='Mean power (GW)',xlim=(0,23),ylim=(0,70));ax.set_xticks([0,4,8,12,16,20,23]);ax.legend(ncol=2,loc='upper left')
save(fig,'Panel_Net_Load','Residual demand after wind and solar, 2025',['data/panel/Intraday-Net-Load-2025.csv'],list(a.columns),'Hourly arithmetic means; MW to GW','System averages; residual demand is not a shortage measure')
a=pd.read_csv(P/'Mean-Decomposition.csv');groups=[(2023,2024),(2023,2025),(2024,2025)]
fig,ax=T.newfig(3.8);pos=np.arange(3); up=np.zeros(3);dn=np.zeros(3)
for key,label,col in [('volume_lmdi','Volume',T.SLATE),('price_level_lmdi','Average price',T.NAVY),('match_lmdi','Timing match',T.TEAL),('rule_effect','Export rule',T.AMBER)]:
 v=np.array([a[(a.from_year==y)&(a.to_year==z)&(a.component==key)].mean_npv_change.iloc[0]/1e6 for y,z in groups]);bot=np.where(v>=0,up,dn)
 ax.bar(pos,v,bottom=bot,color=col,label=label,width=.55);up+=np.maximum(v,0);dn+=np.minimum(v,0)
tot=np.array([a[(a.from_year==y)&(a.to_year==z)&(a.component=='total_change')].mean_npv_change.iloc[0]/1e6 for y,z in groups]);ax.scatter(pos,tot,marker='D',s=30,color=T.INK,label='Total',zorder=8)
for x,v in zip(pos,tot):ax.annotate(f'{v:+.2f}',(x,v),xytext=(0,-18 if v<0 else 8),textcoords='offset points',ha='center',fontsize=8,fontweight='bold')
ax.axhline(0,color=T.INK,lw=.6);ax.set_xticks(pos);ax.set_xticklabels([f'{y} to {z}' for y,z in groups]);ax.set_ylabel('Mean NPV change ($m)');ax.set_ylim(-215,60);ax.legend(ncol=3,loc='upper left',fontsize=7)
save(fig,'Panel_Mean_Decomposition','Mean contributions add to the mean total',['data/panel/Mean-Decomposition.csv'],list(a.columns),'Select four accounting components; means; USD to million','485 nodes; accounting contributions, not causal effects')
a=pd.read_csv(D/'data/scenario_metrics.csv');fig,ax=T.newfig(3.5);y=np.arange(6)
names=['Node: base','Node: downside','Node: upside','Fixed: base','Fixed: downside','Fixed: upside']
for delta,rate,col in [(-.22,'0.0427',T.TEAL),(0,'0.0600',T.NAVY),(.22,'0.0800',T.SLATE)]:
 ax.barh(y+delta,a['npv_real_at_'+rate]/1e6,height=.2,color=col,label={'0.0427':'4.27% real','0.0600':'6% real','0.0800':'8% real'}[rate])
ax.set_yticks(y);ax.set_yticklabels(names);ax.invert_yaxis();ax.set_xlabel('NPV ($m, real 2025 dollars)');ax.set_xlim(-145,0);ax.legend(ncol=3,loc='lower left',bbox_to_anchor=(0,-.32));ax.axvline(0,color=T.INK)
save(fig,'Panel_Scenario_NPV','All six 2025 scenarios have negative NPV',['data/scenario_metrics.csv'],['scenario_id','npv_real_at_0.0427','npv_real_at_0.0600','npv_real_at_0.0800'],'Frozen values; USD to million')
fig,ax=T.newfig(2.7);ax.set_axis_off()
texts=[('Manufacture','Technology, price,\ncapacity and output'),('Overseas supply','Operational factory,\nmaterials and ownership'),('U.S. entry','Classification, origin,\nentry date and duties'),('Project purchase','Delivered quote, warranty,\nEPC and eligible basis')]
for i,(title,body) in enumerate(texts):
 x=.008+i*.25
 ax.add_patch(FancyBboxPatch((x,.19),.224,.62,boxstyle='round,pad=0.006,rounding_size=0.015',fc='#E8EFF3',ec=T.SLATE,lw=.7,transform=ax.transAxes))
 ax.text(x+.112,.66,title,transform=ax.transAxes,ha='center',va='center',fontweight='bold',fontsize=8,color=T.NAVY)
 ax.text(x+.112,.42,body,transform=ax.transAxes,ha='center',va='center',fontsize=7,linespacing=1.7)
 if i<3:ax.annotate('',xy=(x+.245,.5),xytext=(x+.228,.5),xycoords='axes fraction',arrowprops=dict(arrowstyle='->',color=T.TEAL))
save(fig,'Panel_Supply_Route','Four separate evidence links in U.S. procurement',[],[],'Conceptual diagram; no quantitative series','Factory location alone establishes neither duty treatment nor credit eligibility')
(D/'support/Panel-Figure-Lineage.json').write_text(json.dumps(lineage,indent=2))
print('Rendered',len(lineage),'new exhibits')
