import episimmer.model as model


class UserModel(model.StochasticModel):
	def __init__(self):

		beta=0.05
		delta=0.05
		sigma=0.3
		beta1=0.3
		k0=0.2
		mu=0.2
		kt=0.3
		kt1=0.3
		kt2=0.3
		gamma1=0.3
		gamma2=0.3
		gamma3=0.3

		individual_types=['S','A','I','P','R','E','XS','XA','XI','XE']
		infected_states=[]
		state_proportion={
							'S':1
						}
		model.StochasticModel.__init__(self,individual_types,infected_states,state_proportion)
		self.set_transition('S','A',self.p_standard(beta))
		self.set_transition('A','I',self.p_standard(sigma))
		self.set_transition('XS','XA',self.p_standard(beta1*beta))
		self.set_transition('XA','XI',self.p_standard(sigma))
		self.set_transition('S','XS',self.p_standard(k0))
		self.set_transition('XS','S',self.p_standard(mu))
		self.set_transition('A','XA',self.p_standard(k0))
		self.set_transition('XA','A',self.p_standard(mu))
		self.set_transition('E','XE',self.p_standard(k0))
		self.set_transition('XE','E',self.p_standard(mu))
		self.set_transition('I','XI',self.p_standard(k0))
		self.set_transition('XI','I',self.p_standard(mu))
		self.set_transition('S','E',self.p_standard(delta))
		self.set_transition('XS','XE',self.p_standard(beta1*delta))
		self.set_transition('I','P',self.p_standard(kt))
		self.set_transition('XI','P',self.p_standard(kt))
		self.set_transition('A','P',self.p_standard(kt2))
		self.set_transition('XA','P',self.p_standard(kt2))
		self.set_transition('E','P',self.p_standard(kt1))
		self.set_transition('XE','P',self.p_standard(kt1))
		self.set_transition('P','R',self.p_standard(gamma3))
		self.set_transition('I','R',self.p_standard(gamma2))
		self.set_transition('XI','R',self.p_standard(gamma2))
		self.set_transition('E','R',self.p_standard(gamma1))
		self.set_transition('XE','R',self.p_standard(gamma1))


		self.name='Probablistic Lockdown Model'
