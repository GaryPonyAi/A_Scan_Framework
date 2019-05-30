"""
Definition of all the training options
"""

import os
import tensorflow as tf
import pudb

flags = tf.app.flags.FLAGS

tf.app.flags.DEFINE_string('base_dir', None, '')

tf.app.flags.DEFINE_string(
  'labels',
  'background,green,red,yellow,black,green_night,red_night,yellow_night,black_night',
  'The labels')

tf.app.flags.DEFINE_string('tfrecords_generate_mode', 'generate_train_val',
                           'one of [generate_train_val, generate_single_tfrecords]')
tf.app.flags.DEFINE_string('training_data_train_dir', None, '')
tf.app.flags.DEFINE_string('training_data_val_dir', None, '')
tf.app.flags.DEFINE_string('tfrecords_train', None, '')
tf.app.flags.DEFINE_string('tfrecords_val', None, '')
tf.app.flags.DEFINE_string('mean_file', None, '')

tf.app.flags.DEFINE_string('training_data_single_dir', None, '')
tf.app.flags.DEFINE_string('tfrecords_single_path', None, '')

tf.app.flags.DEFINE_integer('batch_size', 256, """Batch size of input data""")

tf.app.flags.DEFINE_integer('train_steps', 10000, "")

# TRAINING_DATA_TRAIN_DIR = os.path.join(flags.training_data_dir, "traffic_light_train", "train")
# TRAINING_DATA_VAL_DIR = os.path.join(flags.training_data_dir, "traffic_light_val", "train")

# print("LABELS={}".format(LABELS))

# tf.app.flags.DEFINE_string('data_folder', '//jianwei/output_nansha,//jianwei/output_fremont',
#                            """Directory to the foreground data""")
# tf.app.flags.DEFINE_string('tfrecords_folder', '/blob/demon/tfrecords_20181127_20',
#                            """Directory to the foreground data""")
# tf.app.flags.DEFINE_float('training_set_percentage', 0.9, """start learning rate""")
#
tf.app.flags.DEFINE_boolean('delete_checkpoint_dir_before_train', True, "")
tf.app.flags.DEFINE_boolean('restore_session', False,
                            """if restore previous session in checkpoint_path""")
tf.app.flags.DEFINE_boolean('reset_global_step_after_restore', True,
                            """Whether to reset global step after restore.""")
tf.app.flags.DEFINE_integer('max_steps', 400000,
                            """Max step to training""")
tf.app.flags.DEFINE_integer('decay_steps', 100000, '')
tf.app.flags.DEFINE_float('decay_rate', 0.1, '')
tf.app.flags.DEFINE_integer('num_steps_train_summary', 16,
                            """Steps to write summary for training phase.""")
tf.app.flags.DEFINE_integer('num_steps_test_summary', 256,
                            """Steps to write summary for test phase.""")

# tf.app.flags.DEFINE_integer('num_steps_test', 500,
#                             """Steps to test""")
# tf.app.flags.DEFINE_integer('num_steps_checkpoint', 1000,
#                             """Steps to write checkpoint""")
tf.app.flags.DEFINE_float('base_learning_rate', 0.1,
                          """start learning rate""")
tf.app.flags.DEFINE_float('momentum', 0.9, '')
tf.app.flags.DEFINE_boolean('use_nesterov', True, '')
tf.app.flags.DEFINE_float('weight_decay', 0.0005, '')
tf.app.flags.DEFINE_float('batch_norm_momentum', 0.95, '')
tf.app.flags.DEFINE_float('batch_norm_epsilon', 1e-5, '')

tf.app.flags.DEFINE_integer('gpu_id', 2, '')
tf.app.flags.DEFINE_boolean('log_device_placement', False, '')
tf.app.flags.DEFINE_boolean('allow_growth', False, '')

# Flags for evaluation:
tf.app.flags.DEFINE_string('evaluation_mode', 'evaluation_and_visualization',
                           'Can be one of [examine_tfrecords, evaluation, evaluation_and_visualization, evaluation_and_move_bad_data]')
tf.app.flags.DEFINE_boolean('evaluation_wait_for_model', True, '')
tf.app.flags.DEFINE_integer('evaluation_visualization_num_pages_per_class', 100, '')

tf.app.flags.DEFINE_float('evaluation_bad_data_softmax_threshold', 0.99, "")

tf.app.flags.DEFINE_string('training_data_dir', None, '')
tf.app.flags.DEFINE_string('tfrecords_dir', None, '')
tf.app.flags.DEFINE_string('checkpoint_dir', None, '')
tf.app.flags.DEFINE_string('previous_model', None, '')
tf.app.flags.DEFINE_string('evaluation_tfrecords', None, '')
tf.app.flags.DEFINE_string('evaluation_output_visualization_dir', None, '')
tf.app.flags.DEFINE_string('evaluation_bad_data_target_dir', None, '')
tf.app.flags.DEFINE_string('output_uff', None, '')

# Flags augmentation
flags.labels = flags.labels.split(",")

flags.training_data_dir = flags.base_dir
flags.tfrecords_dir = os.path.join(flags.base_dir, 'tfrecords')
flags.checkpoint_dir = os.path.join(flags.base_dir, 'checkpoints')
flags.previous_model = os.path.join(flags.checkpoint_dir, 'model.ckpt-60000')
flags.evaluation_tfrecords = os.path.join(flags.tfrecords_dir, 'val.tfrecords')
flags.evaluation_output_visualization_dir = os.path.join(flags.base_dir, 'visualization')
flags.evaluation_bad_data_target_dir = os.path.join(flags.base_dir, 'bad_data')
flags.output_uff = os.path.join(flags.base_dir, 'uff/TL.uff')

if not flags.training_data_train_dir:
  flags.training_data_train_dir = os.path.join(flags.training_data_dir,
                                               'traffic_lights')
if not flags.training_data_val_dir:
  flags.training_data_val_dir = os.path.join(flags.training_data_dir,
                                             'traffic_lights')
if not flags.tfrecords_train:
  flags.tfrecords_train = os.path.join(flags.tfrecords_dir, 'train.tfrecords')
if not flags.tfrecords_val:
  flags.tfrecords_val = os.path.join(flags.tfrecords_dir, 'val.tfrecords')
if not flags.mean_file:
  flags.mean_file = os.path.join(flags.tfrecords_dir, 'mean.npy')

print("=== Flags ===")
for item in flags.flag_values_dict().items():
  print("--{}: {}".format(item[0], item[1]))
