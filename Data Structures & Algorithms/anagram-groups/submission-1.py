class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        
        for word in strs:
            count = [0] * 26

            for letter in word:
                # sacando el unicode de la letra
                index = ord(letter) - ord("a")
                # sumandole 1 a la posicion de la letra en el array
                count[index] += 1
            
            # convertimos a tupla para poder añadir al diccionario
            key = tuple(count)

            # si la tupla llave no existe en el diccionario, la añadimos
            if key not in dictionary:
                dictionary[key] = []

            # añadimos todas las palabras que comparten llave como valor
            dictionary[key].append(word)

        print(dictionary)
        print(key)
        print(count)

        # regresamos todos los valores del diccionario como lista
        return list(dictionary.values())
        