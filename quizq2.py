import numpy as np 

def viterbi(states,obs_seq,trans_mat,em_mat,pri_prob):
    n_states=len(states)
    n_obs=len(obs_seq)
    vit_mat=np.zeros((n_states,n_obs),dtype='float')
    backpointer=np.zeros((n_states,n_obs),dtype='int')

    for i in range(len(states)):
        vit_mat[i][0]=pri_prob[states[i]]*em_mat[states[i]][obs_seq[i]]
        backpointer[i][0]=0
    
    for t in range(1,n_obs):
        for s in range(n_states):
            max_prob=-1
            best_prev=0
            for prev_state in range(n_states):
                prob=vit_mat[prev_state][t-1]*em_mat[states[s]][obs_seq[t]]*trans_mat[states[prev_state]][states[s]]
                if(prob>max_prob):
                    max_prob=prob
                    best_prev=prev_state
            vit_mat[s][t]=max_prob
            backpointer[s][t]=best_prev
    
    best_seq=[]
    last_state=np.argmax(vit_mat[:][-1])
    best_seq.append(states[last_state])

    for i in range(n_obs-1,0,-1):
        last_state=backpointer[last_state][i]
        best_seq.insert(0,states[last_state])

    return best_seq,vit_mat

states=['Rainy','Sunny']
obs_seq=['walk','shop','clean']
trans_mat={
    'Rainy':{'Rainy':0.7,'Sunny':0.3},
    'Sunny':{'Rainy':0.4,'Sunny':0.6}
}
em_mat={
    'Rainy':{'walk':0.1,'shop':0.4,'clean':0.5},
    'Sunny':{'walk':0.6,'shop':0.3,'clean':0.1}
}
pri_prob={'Rainy':0.6,'Sunny':0.4}

ans_seq,vit_mat=viterbi(states,obs_seq,trans_mat,em_mat,pri_prob)
print(ans_seq)
print(vit_mat)