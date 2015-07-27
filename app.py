import web
import rospy
from std_msgs.msg import String


urls = ('/', 'tutorial')
render = web.template.render('templates/')

app = web.application(urls, globals())

topics_and_types = rospy.get_published_topics()
print topics_and_types
dropdown_args = []
for idx, topic_and_type in enumerate(topics_and_types):
    dropdown_args.append(topic_and_type[0])
print dropdown_args


my_form = web.form.Form(
                web.form.Textbox('topic name to publish a std_msgs/String', class_='topic_name_class', id='topic_name'),
                web.form.Textbox('content string', class_='content_class', id='content'),
                web.form.Dropdown('current topics', args=dropdown_args, value='0', class_="dropdown_class", id='dropdown_id')
                )


class tutorial:
    def GET(self):
        form = my_form()
        return render.tutorial(form, "Your text goes here.")
        
    def POST(self):
        form = my_form()
        form.validates()
        topic = form.value['topic_name']
        content = form.value['content']
        if not topic.startswith('/'):
            topic = '/' + topic
        pub = rospy.Publisher(topic, String, latch=True)
        pub.publish(String(content))
        feedback = "Published in " + topic + " the content: " + content
        return feedback

if __name__ == '__main__':
    rospy.init_node('webnode')
    app.run()

