def Convert_M_To_KM(m):
    km = m * 1.60934
    return km

m_input = float(input('Input the miles to convert to kilometers: '))

conv_km = Convert_M_To_KM(m_input)

print(str(conv_km), 'kilometers')
