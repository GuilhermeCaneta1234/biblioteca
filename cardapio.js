import React, { useState } from 'react';
import { View, Text, TouchableOpacity, Image, StyleSheet, FlatList } from 'react-native';

export default function App() {
  const [products] = useState([
    { id: '1', name: 'Hambúrguer', image: 'https://www.estadao.com.br/resizer/v2/77XTHHCCLBEXLC2Y5RK4PN37CE.jpg?quality=80&auth=a86d285f74ec7c08de7ba6ec10d557a463d905ffec2e56009d737687ac6054a1&width=720&height=410&focal=553,494' },
    { id: '2', name: 'Pizza', image: 'https://www.minhareceita.com.br/app/uploads/2022/12/Dpizza-de-pepperoni-caseira-portal-minha-receita.jpg' },
    { id: '3', name: 'Batata Frita', image: 'https://www.estadao.com.br/resizer/v2/SHJEVWJAMBLGHNNFD2RA7RFY2U.jpg?quality=80&auth=df613dd547c609c4169132c5964309806cb21d7c5bf4bf50f851a3d5d81854eb&width=720&height=410&smart=true' },
    { id: '4', name: 'Refrigerante', image: 'https://s2.glbimg.com/GUda5oj9xkd_yQNyn36mDn9XJmo=/620x455/e.glbimg.com/og/ed/f/original/2018/08/17/beber-refrigerante-todos-os-dias-esta-te-matando.jpg' },
    { id: '5', name: 'Suco Natural', image: 'https://www.estadao.com.br/resizer/v2/77XTHHCCLBEXLC2Y5RK4PN37CE.jpg?quality=80&auth=a86d285f74ec7c08de7ba6ec10d557a463d905ffec2e56009d737687ac6054a1&width=720&height=410&focal=553,494' },
    { id: '6', name: 'Sobremesa', image: 'https://www.estadao.com.br/resizer/v2/77XTHHCCLBEXLC2Y5RK4PN37CE.jpg?quality=80&auth=a86d285f74ec7c08de7ba6ec10d557a463d905ffec2e56009d737687ac6054a1&width=720&height=410&focal=553,494' },
  ]);

  const handleBuy = (productName) => {
    alert(`Você pediu: ${productName} 🍽`);
  };

  const renderItem = ({ item }) => (
    <View style={styles.card}>
      <Image source={{ uri: item.image }} style={styles.image} />
      <Text style={styles.name}>{item.name}</Text>
      <TouchableOpacity
        style={styles.button}
        onPress={() => handleBuy(item.name)}
      >
        <Text style={styles.buttonText}>Pedir</Text>
      </TouchableOpacity>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>🍔 Cardápio da Lanchonete</Text>
      <FlatList
        data={products}
        renderItem={renderItem}
        keyExtractor={(item) => item.id}
        numColumns={2}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    paddingTop: 40,
    alignItems: 'center',
  },
  title: {
    fontSize: 22,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  card: {
    backgroundColor: '#f2f2f2',
    borderRadius: 8,
    margin: 10,
    padding: 10,
    alignItems: 'center',
    flex: 1,
  },
  image: {
    width: 120,
    height: 120,
    borderRadius: 8,
    marginBottom: 10,
  },
  name: {
    fontSize: 16,
    marginBottom: 10,
    fontWeight: 'bold',
  },
  button: {
    backgroundColor: '#FF5722',
    paddingVertical: 8,
    paddingHorizontal: 12,
    borderRadius: 8,
  },
  buttonText: {
    color: '#fff',
    fontWeight: 'bold',
  },
});
