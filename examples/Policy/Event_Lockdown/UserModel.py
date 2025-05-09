import episimmer.model as model


def event_contribute_fn(agent,event_info,location,current_time_step):
	if agent.state=='Infected':
		return 1
	return 0


def event_receive_fn(agent,ambient_infection,event_info,location,current_time_step):
	beta=0.1
	return ambient_infection*beta


class UserModel(model.StochasticModel):
	def __init__(self):
		individual_types=['Susceptible','Infected','Recovered']
		infected_states=['Infected']
		state_proportion={
							'Susceptible':0.6,
							'Infected':0.4,
							'Recovered':0
						}
		model.StochasticModel.__init__(self,individual_types,infected_states,state_proportion)
		self.set_transition('Susceptible', 'Infected', self.p_infection())
		self.set_transition('Infected', 'Recovered', self.p_standard(0.2))


		self.set_event_contribution_fn(event_contribute_fn)
		self.set_event_receive_fn(event_receive_fn)

		self.name='Stochastic SIR'
