import matplotlib.pyplot as plt
from matplotlib.testing.decorators import image_comparison

@image_comparison(baseline_images=['hyphen_type'],
                  extensions=['png'])
def test_hyphen():
	math = u'math_part: ${-}$'
	non_math = u'non_math_part: -'
	plt.text(0.5, 0.5, non_math)
	plt.text(0.5, 0.3, non_math + '  ' + math)
