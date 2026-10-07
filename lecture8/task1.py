frontend_skills = {"HTML", "CSS", "JavaScript", "React"}
backend_skills = {"Python", "JavaScript", "SQL", "React"}

print ("All skills:", frontend_skills | backend_skills )
print ("Common skills:" , frontend_skills & backend_skills ) 
print ("Frontend only:" , frontend_skills - backend_skills )
print ("Different skills:" , frontend_skills ^ backend_skills)