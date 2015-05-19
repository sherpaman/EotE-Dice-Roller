#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# Author: Andrea Coletta, PhD
# 
#         Aarhus Universitet, Institut for Kemi
#         Langelandsgade, 140 - Building 1530, Room 417 
#         8000 Aarhus C (Denmark)
#
# Last Update : 19/05/2015
#
import numpy as np
from random import randint
from Tkinter import *

class val:
	def __init__(self,s=0,f=0,a=0,th=0,tr=0,d=0):
		self.s   = s
		self.f   = f
		self.a   = a
		self.th  = th
		self.tr  = tr
		self.d   = d
		self.ns  = 0
		self.nf  = 0
		self.na  = 0
		self.nth = 0
		self.ntr = 0 
		self.nd  = 0

	def __str__(self):
		string="Succ.= %d | Fail.= %d | Adv.= %d | Threat= %d | Triumph= %d | Desp.= %d "  % (self.s,self.f,self.a,self.th,self.tr,self.d)
		return string

	def __add__(self,other):
		s  = self.s  + other.s
		f  = self.f  + other.f
		a  = self.a  + other.a
		th = self.th + other.th
		tr = self.tr + other.tr
		d  = self.d  + other.d
		out = val(s,f,a,th,tr,d)
		out.net()
		return out

	def __mul__(self,other):
		s  = self.s  * other
		f  = self.f  * other
		a  = self.a  * other
		th = self.th * other
		tr = self.tr * other
		d =  self.d  * other
		return val(s,f,a,th,tr,d)

	def __rmul__(self,other):
		s  = self.s  * other
		f  = self.f  * other
		a  = self.a  * other
		th = self.th * other
		tr = self.tr * other
		d =  self.d  * other
		return val(s,f,a,th,tr,d)

	def __imul__(self,other):
		s  = self.s  * other
		f  = self.f  * other
		a  = self.a  * other
		th = self.th * other
		tr = self.tr * other
		d =  self.d  * other
		return val(s,f,a,th,tr,d)
	
	def __rdiv__(self,other):
		s  = self.s  / other
		f  = self.f  / other
		a  = self.a  / other
		th = self.th / other
		tr = self.tr / other
		d =  self.d  / other
		return val(s,f,a,th,tr,d)
	
	def __div__(self,other):
		s  = self.s  / other
		f  = self.f  / other
		a  = self.a  / other
		th = self.th / other
		tr = self.tr / other
		d =  self.d  / other
		return val(s,f,a,th,tr,d)
	
	def net(self):
		ns       = self.s  - self.f + self.tr - self.d
		na       = self.a  - self.th
		ntr      = self.tr
		nd       = self.d
		self.ns  = max(0,  ns)
		self.nf  = max(0, -ns)
		self.na  = max(0,  na)
		self.nth = max(0, -na)
		self.ntr = self.ntr
		self.nd  = self.nd
	
	def check_net(self):
		self.net()
		string="Succ.= %d | Fail.= %d | Adv.= %d | Threat= %d | Triumph= %d | Desp.= %d "  % (self.ns,self.nf,self.na,self.nth,self.ntr,self.nd)
		print string
	
	def string_net(self):
		self.net()
		return "Succ.= %d | Fail.= %d | Adv.= %d | Threat= %d | Triumph= %d | Desp.= %d "  % (self.ns,self.nf,self.na,self.nth,self.ntr,self.nd)

class dice:
	def __init__(self,name="ability"):
		self.name     = name
		self.dim      = self.dim()
		self.outcomes = self.out()
	
	def dim(self):
		dice_dim={"boost":6,"setback":6,"ability":8,"difficulty":8,"proficiency":12,"challenge":12}
		return dice_dim[(self.name)]
	
	def out(self):
		if   ( self.name == "boost" ):
			return [val(),val(),val(s=1),val(s=1,a=1),val(a=2),val(a=1)]
		elif ( self.name == "setback" ):
			return [val(),val(),val(f=1),val(f=1),val(th=1),val(th=1)]
		elif ( self.name == "ability" ):
			return [val(),val(s=1),val(s=1),val(s=2),val(a=1),val(a=1),val(s=1,a=1),val(a=2)]
		elif ( self.name == "difficulty" ):
			return [val(),val(f=1),val(f=2),val(th=1),val(th=1),val(th=1),val(th=2),val(f=1,th=1)]
		elif ( self.name == "proficiency" ):
			return [val(),val(s=1),val(s=1),val(s=2),val(s=2),val(a=1),val(s=1,a=1),val(s=1,a=1),val(s=1,a=1),val(a=2),val(a=2),val(tr=1)]
		elif ( self.name == "challenge" ):
			return [val(),val(f=1),val(f=1),val(f=2),val(f=2),val(th=1),val(th=1),val(f=1,th=1),val(f=1,th=1),val(th=2),val(th=2),val(d=1)]
			
	def trow(self,num=1):
		result=val()
		for i in range(num):
			result=result+self.outcomes[randint(0,self.dim-1)]
		return result

class pool:
	def __init__(self,A=1,D=0,B=0,S=0,P=0,C=0):
		self.num = [int(A),int(D),int(B),int(S),int(P),int(C)]
		self.A = int(A)
		self.D = int(D)
		self.B = int(B)
		self.S = int(S)
		self.P = int(P)
		self.C = int(C)
		self.dices = [dice("ability"),dice("difficulty"),dice("boost"),dice("setback"),dice("proficiency"),dice("challenge")]
		self.values = [val(),val(),val(),val(),val(),val()]
		self.result = val()
		
	def trow(self):
		self.result=val()
		for d in range(6):
			self.values[d] = self.dices[d].trow(self.num[d])
			self.result += self.values[d]
		return self.result
		
if __name__ == "__main__":
	import numpy as np
	from random import randint
	from Tkinter import *
	class Dice_Launcher(Frame):
		def __init__ (self,master):
			Frame.__init__(self,master)
			self.grid()
			self.create_window()
			
		def create_window(self):
			self.Launch = Button(self,text="May the Force be with you!",command=self.launch_dices)
			self.Calc   = Button(self,text="Evaluate Chances",command=self.calc_prob)
			
			self.A_label = Label(self, text = "Ability :")
			self.D_label = Label(self, text = "Difficulty :")
			self.B_label = Label(self, text = "Boost :")
			self.S_label = Label(self, text = "Setback :")
			self.P_label = Label(self, text = "Proficiency :")
			self.C_label = Label(self, text = "Challenge :")
			self.A = Entry(self)
			self.D = Entry(self)
			self.B = Entry(self)
			self.S = Entry(self)
			self.P = Entry(self)
			self.C = Entry(self)
			
			self.Result      = Text(self, height = 2)
			self.Probability = Text(self, height = 12)
			
			self.A_label.grid(row=1,column=0); self.A.grid(row=1,column=1)
			self.D_label.grid(row=2,column=0); self.D.grid(row=2,column=1)
			self.B_label.grid(row=3,column=0); self.B.grid(row=3,column=1)
			self.S_label.grid(row=4,column=0); self.S.grid(row=4,column=1)
			self.P_label.grid(row=5,column=0); self.P.grid(row=5,column=1)
			self.C_label.grid(row=6,column=0); self.C.grid(row=6,column=1)
			
			self.Launch.grid(row=7,column=0,columnspan=2)
			self.Calc.grid(row=8,column=0,columnspan=2)
			self.Result.grid(row=9,column=0,rowspan=2,columnspan=2)
			self.Probability.grid(row=12,column=0,rowspan=12,columnspan=2)
		
		def read_entries(self):
			inp = [self.A.get(),self.D.get(),self.B.get(),self.S.get(),self.P.get(),self.C.get()]
			for i in range(6):
				if inp[i] == "":
					inp[i] = 0
				else:
					inp[i]=int(inp[i])
			return inp

		def launch_dices(self):
			inp = self.read_entries()
			dices_pool = pool(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5])
			result     = dices_pool.trow()
			self.Result.delete(0.0,END)
			self.Result.insert(0.0,result.string_net())
		
		def calc_prob(self):
			inp = self.read_entries()
			num_trial = 50000
			dices_pool = pool(inp[0],inp[1],inp[2],inp[3],inp[4],inp[5])
			p_s  = 0.0
			p_f  = 0.0
			p_a  = 0.0
			p_th = 0.0
			p_tr = 0.0
			p_d  = 0.0
			
			succ = 0
			fail = 0
			adv  = 0
			thre = 0
			
			for t in np.arange(num_trial):
				trial = dices_pool.trow()
				if trial.ns > 0:
					p_s  += 1
					succ += trial.ns
				else:
					p_f  += 1
					fail += trial.f
				if trial.a > 0 :
					p_a += 1
					adv += trial.a
				elif trial.th > 0:
					p_th += 1
					thre += trial.th
				if trial.tr > 0:
					p_tr += 1
				if trial.d > 0:
					p_d += 1
			succ = float(succ) / p_s
			fail = float(fail) / p_f
			adv  = float(adv)  / num_trial
			thre = float(thre) / num_trial
			p_s  = p_s  / num_trial * 100.0
			p_f  = p_f  / num_trial * 100.0
			p_a  = p_a  / num_trial * 100.0
			p_th = p_th / num_trial * 100.0
			p_tr = p_tr / num_trial * 100.0
			p_d  = p_d  / num_trial * 100.0
			
			self.Probability.delete(0.0,END)
			out=" Prob(S) :%5.1f [Average Successes  (When succeeding) : %5.1f]\n Prob(F) :%5.1f [Average Failures   (When failing)    : %5.1f]\n Prob(A) :%5.1f [Average Advantages (Overall)         : %5.1f]\n Prob(Th):%5.1f [Average Threats    (Overall)         : %5.1f]\n Prob(Tr):%5.1f\n Prob(D) :%5.1f" %(p_s,succ,p_f,fail,p_a,adv,p_th,thre,p_tr,p_d) 
			self.Probability.insert(0.0,out)

	root = Tk()
	root.title("Edge of the Empire Dice Roller")
	root.geometry("600x500")
	
	app=Dice_Launcher(root)
	root.mainloop()
