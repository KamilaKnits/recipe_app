from io import BytesIO
import base64
import matplotlib.pyplot as plt

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_chart(chart_type, data):

    plt.switch_backend('AGG')
    plt.figure(figsize=(7,7))

    if chart_type == '#1': # bar chart
        plt.bar(data['name'], data['cooking_time'])
        plt.title('Cooking Time by Recipe')
        plt.xlabel('Recipe Name')
        plt.ylabel('Cooking Time (minutes)')
        plt.xticks(rotation=45,ha='right')  #rotate and right align
        plt.subplots_adjust(bottom=0.25)
 
    elif chart_type == '#2': # pie chart
        difficulty_list = data['difficulty']
        labels = ['Easy', 'Medium', 'Intermediate', 'Hard']
        sizes = [difficulty_list.count(label) for label in labels]
        unique_difficulties = set(difficulty_list)

        if len(unique_difficulties) <=1:
            plt.text(0.5, 0.5, 'Not enough data', ha='center', fontsize=12)
        else:
            plt.pie(sizes, labels = labels, autopct='%1.1f%%', startangle=90)
            plt.title('Difficulty')

    elif chart_type == '#3':  # line plot
        difficulty_map = {'Easy': 1, 'Medium': 2, 'Intermediate': 3, 'Hard': 4}
        difficulty_numeric = [difficulty_map.get(d,0) for d in data['difficulty']]
        plt.scatter(data['cooking_time'], difficulty_numeric, marker='s')
        plt.title('Cooking Time vs Difficulty')
        plt.xlabel('Cooking Time (minutes)')
        plt.ylabel('Difficulty Level')
        plt.yticks([1,2,3,4], ['Easy', 'Medium', 'Intermediate', 'Hard'])

    else:
        plt.text(0.5, 0.5, 'unknown chart type', ha='center')
    
    plt.tight_layout() # specify layout
    chart = get_graph() # render graph to to file
    return chart 
