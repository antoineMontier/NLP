## Embedding layer

**Keras** offers us the `Embedding` layer with those arguments:

- input_dim: Integer. Size of the vocabulary, i.e. maximum integer index + 1.

- output_dim: Integer. Dimension of the dense embedding.

- embeddings_initializer: Initializer for the embeddings matrix (see keras.initializers).

- embeddings_regularizer: Regularizer function applied to the embeddings matrix (see keras.regularizers).

- embeddings_constraint: Constraint function applied to the embeddings matrix (see keras.constraints).

- mask_zero: Boolean, whether or not the input value 0 is a special "padding" value that should be masked out.

This is useful when using recurrent layers which may take variable length input. If this is True, then all subsequent layers in the model need to support masking or an exception will be raised. If mask_zero is set to True, as a consequence, index 0 cannot be used in the vocabulary (input_dim should equal size of vocabulary + 1).

> Source: [Keras' documentation](https://keras.io/api/layers/core_layers/embedding/)

Go back to the [presentation](./README.md#under-the-iceberg)