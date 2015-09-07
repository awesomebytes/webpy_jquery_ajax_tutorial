import web
import rospy
from dynamic_reconfigure import client as drc
from dynamic_reconfigure import find_reconfigure_services


urls = ('/', 'tutorial',
        '/client', 'dynrecclient')
render = web.template.render('templates/')

app = web.application(urls, globals())


# TODO: Send to another page that in the url you specify
# the dynamic reconfigure server name
# and shows all the stuff




class tutorial:

    def __init__(self):
        self.dynamic_reconfigure_servers = None
        self.my_form = None

    def create_form(self):
        self.dynamic_reconfigure_servers = find_reconfigure_services()
        print "Found dynamic reconfigure servers:\n" + str(self.dynamic_reconfigure_servers)
        dropdown_args = []
        for idx, server_name in enumerate(self.dynamic_reconfigure_servers):
            dropdown_args.append(server_name)
        print dropdown_args
        self.my_form = web.form.Form(
                        # web.form.Textbox('topic name to publish a std_msgs/String', class_='topic_name_class', id='topic_name'),
                        # web.form.Textbox('content string', class_='content_class', id='content'),
                        web.form.Dropdown('Dynamic Reconfigure Servers:', args=dropdown_args, value='0', class_="dropdown_class", id='dropdown_id')
                        )

    def GET(self):
        self.create_form()
        form = self.my_form()
        return render.tutorial(form, "Your text goes here.")
        
    def POST(self):
        self.create_form()
        form = self.my_form()
        form.validates()
        # topic = form.value['topic_name']
        # content = form.value['content']
        # if not topic.startswith('/'):
        #     topic = '/' + topic
        # pub = rospy.Publisher(topic, String, latch=True)
        # pub.publish(String(content))
        # feedback = "Published in " + topic + " the content: " + content
        feedback = 'this is feedback'
        return feedback

class dynrecclient:

    def __init__(self):
        self.dynamic_reconfigure_servers = None
        self.my_form = None

    def create_form(self):
        self.dynamic_reconfigure_servers = find_reconfigure_services()
        print "Found dynamic reconfigure servers:\n" + str(self.dynamic_reconfigure_servers)
        dropdown_args = []
        for idx, server_name in enumerate(self.dynamic_reconfigure_servers):
            dropdown_args.append(server_name)
        print dropdown_args
        self.my_form = web.form.Form(
                        # web.form.Textbox('topic name to publish a std_msgs/String', class_='topic_name_class', id='topic_name'),
                        # web.form.Textbox('content string', class_='content_class', id='content'),
                        web.form.Dropdown('Dynamic Reconfigure Servers:', args=dropdown_args, value='0', class_="dropdown_class", id='dropdown_id')
                        )

    def GET(self):
        # for handling http://localhost:8080/client?server=/my_dynamic_reconfigure
        user_data = web.input()
        print "Accesing http://localhost:8080/client?server="
        print user_data.server
        self.create_form()
        form = self.my_form()
        return render.tutorial(form, "This is a dynamic reconfigure client of " + str(user_data.server))

    def POST(self):
        self.create_form()
        form = self.my_form()
        form.validates()
        # topic = form.value['topic_name']
        # content = form.value['content']
        # if not topic.startswith('/'):
        #     topic = '/' + topic
        # pub = rospy.Publisher(topic, String, latch=True)
        # pub.publish(String(content))
        # feedback = "Published in " + topic + " the content: " + content
        feedback = 'this is feedback'
        return feedback


if __name__ == '__main__':
    rospy.init_node('webnode')
    app.run()

