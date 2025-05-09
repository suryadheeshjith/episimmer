import episimmer.model as model

#The two functions event_contribute_fn and event_receive_fn together control the spread of infection

# This function states the amount an agent contributes to ambient infection in the region
#note that only infected agents contibute to the ambient infection
def event_contribute_fn(agent,event_info,location,current_time_step):
	if agent.state=='Infected':
		return 1
	return 0

#This function states the probability of an agent becoming infected from the ambient infection
def event_receive_fn(agent,ambient_infection,event_info,location,current_time_step):
	beta=0.001
	return ambient_infection*beta


class UserModel(model.StochasticModel):
	def __init__(self):
		individual_types=['Susceptible','Infected','Recovered']	#These are the states that will be used by the compartmental model
		infected_states=['Infected']	#These are the states that can infect
		state_proportion={				#This is the starting proportions of each state
							'Susceptible':0.99,
							'Infected':0.01,
							'Recovered':0
						}
		model.StochasticModel.__init__(self,individual_types,infected_states,state_proportion)  #We use the inbuilt model in the package
		self.set_transition('Susceptible', 'Infected', self.p_infection())	#Adding S-> I dependent transition
		self.set_transition('Infected', 'Recovered', self.p_standard(0.2))	#Adding the I->R independent transition


		self.set_event_contribution_fn(event_contribute_fn)
		self.set_event_receive_fn(event_receive_fn)

		self.name='Stochastic SIR'
