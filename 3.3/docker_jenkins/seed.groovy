import jenkins.model.Jenkins
import hudson.security.HudsonPrivateSecurityRealm
import hudson.security.FullControlOnceLoggedInAuthorizationStrategy
import hudson.model.FreeStyleProject
import hudson.tasks.Shell
def j=Jenkins.get()
j.setSecurityRealm(new HudsonPrivateSecurityRealm(false))
def auth=new FullControlOnceLoggedInAuthorizationStrategy()
auth.setAllowAnonymousRead(true)
j.setAuthorizationStrategy(auth)
j.setSlaveAgentPort(-1)
j.setNumExecutors(1)
j.setSystemMessage('NIASPO 3.3 — Maxim Kuznetsov. Read-only demonstration. Job configuration is managed from Git.')
def job=j.getItem('hello-container')
if(job==null)job=j.createProject(FreeStyleProject.class,'hello-container')
job.setDescription('Демонстрация автоматического задания Jenkins: команда и версия Java.')
job.getBuildersList().clear()
job.getBuildersList().add(new Shell('echo "Hello from a real Jenkins build!"\necho "Maxim Kuznetsov, IKBO-15-25"\njava -version\n'))
job.save()
j.save()
job.scheduleBuild2(0)
