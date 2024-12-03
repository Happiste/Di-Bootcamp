import seaborn as sns
import matplotlib.pyplot as plt

# Load sample data
data = sns.load_dataset('tips')
sns.histplot(data['total_bill'])
plt.title('Histogram of Total Bill')
plt.show()